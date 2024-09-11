from django.urls import reverse
from djmoney.models.fields import MoneyField
from django.db import models

from BookShop import settings


class Book(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='IRR')
    publisher = models.CharField(max_length=120)
    publication_date = models.DateField()
    description = models.TextField()
    is_exist = models.BooleanField()

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.book.pk})

    def __str__(self):
        return self.comment