from django.db import models
from django.contrib.auth.models import User


class Jugadores(models.Model):
    nombre = models.CharField(max_length = 50)
    edad = models.IntegerField()
    numero = models.IntegerField()
    antiguedad = models.IntegerField()
    ganado = models.CharField(max_length = 150)
    clubes = models.CharField(max_length = 200)

    def __str__(self):
        return f'{self.nombre}'
    
    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'

class Director_tecnico(models.Model):
    nombre = models.CharField(max_length = 50)
    edad = models.IntegerField()
    numero = models.CharField(max_length = 30)
    antiguedad = models.IntegerField()
    ganado = models.CharField(max_length = 150)
    clubes = models.CharField(max_length = 300)

    class Meta:
        verbose_name = 'Director Tecnico'
        verbose_name_plural = 'Directores Tecnicos'

class Tribunas(models.Model):
    nombre = models.CharField(max_length = 50, blank = False)
    capacidad = models.IntegerField(blank = False)
    ingreso = models.CharField(max_length = 150, blank = False)

    def __str__(self):
        return f'{self.nombre}'
    
    class Meta:
        verbose_name = 'Tribuna'
        verbose_name_plural = 'Tribunas'    

class Estadio(models.Model):
    historia = models.CharField(max_length = 100000000000)

    class Meta:
        verbose_name = 'Estadio'
        verbose_name_plural = 'Estadios'

class Socios(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    dni = models.IntegerField()
    email = models.EmailField()
    direccion = models.CharField(max_length = 50)
    numero = models.IntegerField()

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'

    class Meta:
        verbose_name = 'Socio'
        verbose_name_plural = 'Socios'

class Avatar(models.Model):
    imagen = models.ImageField(upload_to = 'avatares')
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user} {self.imagen}'
    

class Quien_Soy(models.Model):
    quien_soy = models.CharField(max_length = 100000)
    class Meta:
        verbose_name = 'Quien Soy'
        verbose_name_plural = 'Quienes Somos'


class Cancion(models.Model):
    nombre = models.CharField(max_length = 30)
    letra = models.CharField(max_length = 100000)

    def __str__(self):
        return f'{self.nombre}'
    
    class Meta:
        verbose_name = 'Cancion'
        verbose_name_plural = 'Canciones'


class Intereses(models.Model):
    intereses = models.CharField(max_length = 100000000)

    def __str__(self):
        return f'{self.intereses}'
    
    class Meta:
        verbose_name = 'Interes'
        verbose_name_plural = 'Intereses'
