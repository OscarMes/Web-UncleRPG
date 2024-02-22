from django.db import models
from django.db.models.fields import CharField, URLField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.
class Cls_juegos(models.Model):
    nombre = CharField(max_length=100)
    sinopsis = TextField()
    imagen = ImageField(upload_to='uncleapp/images/') 
    url_descargar = URLField(blank = True)