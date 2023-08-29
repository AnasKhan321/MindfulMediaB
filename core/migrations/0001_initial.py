# Generated by Django 4.1.10 on 2023-08-25 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=90)),
                ('Category', models.CharField(default='', max_length=40)),
                ('image', models.ImageField(upload_to='bookimg')),
                ('Summary', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(default='', max_length=200)),
                ('Price', models.CharField(default='', max_length=90)),
                ('Update', models.CharField(max_length=200, null=True)),
                ('Address1', models.CharField(default='', max_length=300)),
                ('Address2', models.CharField(default='', max_length=200)),
                ('State', models.CharField(default='', max_length=90)),
                ('City', models.CharField(default='', max_length=90)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address1', models.CharField(default='', max_length=300)),
                ('Address2', models.CharField(default='', max_length=200)),
                ('State', models.CharField(default='', max_length=70)),
                ('City', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]