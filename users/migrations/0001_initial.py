# Generated by Django 4.1.6 on 2023-05-01 20:14

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=20, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(max_length=50, null=True)),
                ('number', models.CharField(max_length=20, null=True)),
                ('sex', models.CharField(choices=[('Мужчина', 'man'), ('Женщина', 'women')], max_length=20)),
                ('img', models.ImageField(height_field=100, upload_to=users.models.user_directory_path, width_field=100)),
                ('date_of_birth', models.DateTimeField(null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('seller', models.CharField(choices=[('Частное лицо', 'private_person'), ('Компания', 'company')], max_length=20)),
                ('exchange', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('user_who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_who', to=settings.AUTH_USER_MODEL)),
                ('user_whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_whom', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
    ]
