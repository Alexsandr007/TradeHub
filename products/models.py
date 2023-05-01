from django.db import models


class Features(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=200)

    class Meta:
        db_table = 'features'


CONDITION_CHOICES = (
    ('Новое', 'new'),
    ('Б/у', 'old')
)


CATEGORY_CHOICES = (
    ('Недвижимость', 'Real estate'),
    ('Авто и транспорт', 'Car and transport'),
    ('Ремонт и стройка', 'Renovation and construction'),
    ('Хобби, спорт и туризм', 'Hobbies, sports and tourism'),
    ('Все для детей и родителей', 'All for children and parents'),
    ('Мебель', 'Furniture'),
    ('Женский гардероб', 'Womens wardrobe'),
    ('Животные', 'Animals'),
    ('Все для дома', 'All for your home'),
    ('Телефоны и планшеты', 'Phones and tablets'),
    ('Сад и огород', 'Garden and vegetable garden'),
    ('Электроника', 'Electronics'),
    ('Компьютерная техника', 'Computer hardware'),
    ('Бытовая техника', 'Household appliances'),
    ('Мужской гардероб', 'Mens wardrobe'),
    ('Услуги', 'Services'),
    ('Готовый бизнес и оборудование', 'Ready-made business and equipment'),
    ('Красота и здоровье', 'Beauty and health'),
    ('Работа', 'Job'),
    ('Свадьбы и праздники', 'Weddings and celebrations'),
    ('Прочее', 'Other'),
)


class Products(models.Model):
    name = models.CharField(max_length=50)
    cost = models.FloatField()
    сondition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    short_description = models.CharField(max_length=50)
    features = models.ForeignKey(Features, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=50)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    class Meta:
        db_table = 'products'
