from django.contrib import admin
from  .models import Order,Details,Books
# Register your models here.
admin.site.register(Order)
admin.site.register(Details)
admin.site.register(Books)