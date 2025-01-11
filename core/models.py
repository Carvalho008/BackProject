from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100, name='nome', verbose_name='Nome')
    email = models.EmailField(unique=True, name='email', verbose_name='E-mail')
    whatsapp = models.CharField(max_length=20, unique=True, name='whatsapp', verbose_name='Whatsapp')
    
    def __str__(self):
        return f'{self.nome} - {self.email} - {self.whatsapp}'