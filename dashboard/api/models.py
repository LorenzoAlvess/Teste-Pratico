from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Library(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateField(auto_now_add=True)
    num_books = models.IntegerField(default=0)


class Book(models.Model):
    library = models.ForeignKey(Library, related_name='books', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    creation_date = models.DateField(auto_now_add=True)


@receiver(post_save, sender=Book)
@receiver(post_delete, sender=Book)
def update_library_num_books(sender, instance, **kwargs):
    library = instance.library
    library.num_books = library.books.count()
    library.save()
