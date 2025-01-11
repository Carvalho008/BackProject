from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100, name='nome')
    email = models.EmailField(unique=True, name='email')
    whatsapp = models.CharField(max_length=20, unique=True, name='whatsapp')
    
    def __str__(self):
        return f'{self.nome} - {self.email} - {self.whatsapp}'