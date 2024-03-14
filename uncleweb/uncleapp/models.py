from django.db import models
from django.db.models.fields import CharField, URLField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.

class Tbl_motor(models.Model):
    nombre = CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Tbl_juegos(models.Model):
    nombre = CharField(max_length=100)
    sinopsis = TextField()
    img = ImageField(upload_to='uncleapp/images/') 
    url_descargar = URLField(blank = True)
    fkidJuegos_idMotor = models.ForeignKey(Tbl_motor, null=True, blank=True, on_delete=models.CASCADE )
    
    def __str__(self):
        return self.nombre


class Tbl_tres_populares(models.Model):
    fkidTrespopulares_idJuegos = models.ForeignKey(Tbl_juegos, null = True, blank = True, on_delete = models.PROTECT)
    img = ImageField(upload_to='uncleapp/images/3_populares')
    posicion = CharField(max_length=25)

    def __str__(self):
        return self.posicion