from django.db import models
from django.utils.safestring import mark_safe
# модель автора.
class Author(models.Model):  
    full_name = models.TextField()  # str
    birth_year = models.SmallIntegerField()  #int
    country = models.CharField(max_length=2)  # ограничение 2 симв
def __str__(self):  
        return self.full_name

# модель книги
class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  #ограничение в 13 симв
    title = models.TextField()
    image = models.ImageField(help_text='20x20px', blank=True)  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #поле внешнего ключа
    copy_count = models.SmallIntegerField(default=1, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=' ')
    redaction = models.ForeignKey('Publish', on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    reader = models.ForeignKey('Reader', on_delete=models.CASCADE, null=True, blank=True, related_name='books')
# модель издательства
class Publish(models.Model):
    name = models.CharField(max_length=100)
def __str__(self):
    return self.name
    # модель читатель
class Reader(models.Model):
    full_name = models.TextField()  # str
    birth_year = models.SmallIntegerField()  #int
    # картинки
@property
def image_img(self):
    if self.image and hasattr(self.image, 'url'):
        return self.image.url