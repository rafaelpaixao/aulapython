from django.db import models
from dj.choices.fields import ChoiceField
from .choices import Category


# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"Nome")
    description = models.TextField(verbose_name=u"Descrição/Ingredientes")
    created = models.DateTimeField(auto_now_add=True, verbose_name=u"Data de criação")
    price = models.DecimalField(decimal_places=2, max_digits=5, verbose_name=u"Preço R$")
    category = ChoiceField(choices=Category, default=Category.normal, verbose_name=u"Categoria")

    def __str__(self):
        return self.name

class Order(models.Model):
    notes = models.TextField(verbose_name=u"Anotação")
    client = models.ForeignKey('auth.User',related_name='orders')

