from django.db import models
from django.utils import timezone

# Create your models here.
# Id (primary key - automatico pelo django)
# first_name (string), last_name(string), phone(string)
# email (email), created_date(date), description(text)

# picture (image)
# category (foreign key), show (boolean), 
# owner (foreign key)


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/', blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    


    