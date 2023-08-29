from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Books, Order, Details
import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from .Seriliazers import BookSerializer, OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
import json

header = {
    "alg": "HS256",
    "typ": "JWT"
}

secret = "bedardaya"


# Create your views here.
def index(request):
    return JsonResponse({"message": "this is meessage "})


@csrf_exempt
def createuser(request):
    if request.method == "POST":

        payload = {
            "name": request.POST['name']
        }

        secret = "bedardaya"
        encoded_jwt = jwt.encode(payload, secret, algorithm='HS256', headers=header)
        print(encoded_jwt)
        decoded_jwt = jwt.decode(encoded_jwt, secret, algorithms=['HS256'])
        print(decoded_jwt)
        print(request.POST['name'])
        return JsonResponse({"auth-token": encoded_jwt})
    else:
        return JsonResponse({"message": "this is get  sage "})


@csrf_exempt
def handleSignup(request):
    if request.method == 'POST':
        bytes_data = request.body

        # Convert bytes to string
        string_data = bytes_data.decode('utf-8')  # Use the appropriate encoding

        # Parse the string as JSON
        json_data = json.loads(string_data)

        # Now you have a Python dictionary containing the JSON data
        print(json_data.get('fname'))
        print(request.body)

        firstName = json_data.get('fname')
        lastName = json_data.get('lname')
        email = json_data.get('email')
        pass1 = json_data.get('pass1')

        username = firstName + lastName

        print(username, firstName, lastName, email, pass1)

        if len(pass1) < 8:
            return JsonResponse({"error": "Password is To Short   "})

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstName
        myuser.last_name = lastName
        myuser.save()
        payload = {
            "id": myuser.id
        }
        encoded_jwt = jwt.encode(payload, secret, algorithm='HS256', headers=header)
        return JsonResponse({"auth": encoded_jwt, "user": myuser.username})


@csrf_exempt
def getuser(request):
    vs = request.POST['auth']

    decoded_jwt = jwt.decode(vs, secret, algorithms=['HS256'])
    print(type(decoded_jwt.get('id')))
    user = User.objects.get(id=decoded_jwt.get('id'))
    print(user.username)
    return JsonResponse({"user": user.username})


@csrf_exempt
def handleLogin(request):
    if request.method == 'POST':
        bytes_data = request.body

        # Convert bytes to string
        string_data = bytes_data.decode('utf-8')  # Use the appropriate encoding

        # Parse the string as JSON
        json_data = json.loads(string_data)

        # Now you have a Python dictionary containing the JSON data
        print(json_data.get('fname'))
        print(request.body)

        username = json_data.get('loginusername')
        password = json_data.get('loginpass')

        print(username, password)
        user1 = authenticate(username=username, password=password)

        if user1 is not None:
            payload = {
                "id": user1.id
            }
            encoded_jwt = jwt.encode(payload, secret, algorithm='HS256', headers=header)
            if not Details.objects.filter(user=user1).exists():
                 return JsonResponse({"auth": encoded_jwt, "user": username,'detail' : 'NO'})
            else:
                return JsonResponse({"auth": encoded_jwt, "user": username, 'detail': 'save'})

        else:
            return JsonResponse({"error": "SignUp First"})


@csrf_exempt
def takeShipment(request):
    if request.method == 'POST':
        bytes_data = request.body

        # Convert bytes to string
        string_data = bytes_data.decode('utf-8')  # Use the appropriate encoding

        # Parse the string as JSON
        json_data = json.loads(string_data)
        vs = json_data.get('auth')

        decoded_jwt = jwt.decode(vs, secret, algorithms=['HS256'])
        user = User.objects.get(id=decoded_jwt.get('id'))
        address1 = json_data.get('address1')
        address2 = json_data.get('address2')
        state = json_data.get('state')
        city = json_data.get('city')
        Detail = Details(user=user, Address1=address1, Address2=address2, State=state, City=city)
        Detail.save()
        return JsonResponse({'detail': 'save'})

@csrf_exempt
def takeOrder(request):
    if request.method == 'POST':
        bytes_data = request.body

        # Convert bytes to string
        string_data = bytes_data.decode('utf-8')  # Use the appropriate encoding

        # Parse the string as JSON
        json_data = json.loads(string_data)
        vs = json_data.get('auth')
        item = json_data.get('item')
        price = json_data.get('price')

        decoded_jwt = jwt.decode(vs, secret, algorithms=['HS256'])
        user = User.objects.get(id=decoded_jwt.get('id'))
        detail = Details.objects.get(user=user)
        o = Order(user=user, item=item, Price=price, Address1=detail.Address1, Address2=detail.Address2,
                  State=detail.State, City=detail.City)
        o.save()
        return JsonResponse({'Order': 'Place Successfully '})


@api_view(('GET',))
def getallbooks(request):
    Book = Books.objects.all()
    serializer = BookSerializer(Book, many=True)
    print(serializer)
    return Response(serializer.data)


@api_view(('GET',))
def getCategoryBook(request, category):
    Book = Books.objects.filter(Category=category)
    print(Book)
    serializer = BookSerializer(Book, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def getorder(request):

        decoded_jwt = jwt.decode(request.headers.get('Auth'), secret, algorithms=['HS256'])
        print(decoded_jwt)
        user = User.objects.get(id=decoded_jwt.get('id'))
        order = Order.objects.filter(user=user)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)
