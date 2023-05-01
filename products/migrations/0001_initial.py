# Generated by Django 4.1.6 on 2023-05-01 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'features',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cost', models.FloatField()),
                ('сondition', models.CharField(choices=[('Новое', 'new'), ('Б/у', 'old')], max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('short_description', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Недвижимость', 'Real estate'), ('Авто и транспорт', 'Car and transport'), ('Ремонт и стройка', 'Renovation and construction'), ('Хобби, спорт и туризм', 'Hobbies, sports and tourism'), ('Все для детей и родителей', 'All for children and parents'), ('Мебель', 'Furniture'), ('Женский гардероб', 'Womens wardrobe'), ('Животные', 'Animals'), ('Все для дома', 'All for your home'), ('Телефоны и планшеты', 'Phones and tablets'), ('Сад и огород', 'Garden and vegetable garden'), ('Электроника', 'Electronics'), ('Компьютерная техника', 'Computer hardware'), ('Бытовая техника', 'Household appliances'), ('Мужской гардероб', 'Mens wardrobe'), ('Услуги', 'Services'), ('Готовый бизнес и оборудование', 'Ready-made business and equipment'), ('Красота и здоровье', 'Beauty and health'), ('Работа', 'Job'), ('Свадьбы и праздники', 'Weddings and celebrations'), ('Прочее', 'Other')], max_length=100)),
                ('features', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.features')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
