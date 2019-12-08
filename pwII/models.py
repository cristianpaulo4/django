from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Endereco(models.Model):
    estado = models.CharField(max_length=100, null=False, blank=False)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    logradouro = models.CharField(max_length=100, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)   
    
    def __str__(self):
        return self.cidade+' - '+ self.estado



class Cliente(models.Model):   
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=100, null=False, blank=False)
    idade = models.CharField(max_length=100, null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)  
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)      
    def __str__(self):
        return self.nome


class Procedimento(models.Model):
    descricao = models.CharField(max_length=100, null=False, blank=False)
    valor = models.FloatField(blank=False, null=False)
    def __str__(self):
        return self.descricao
    
    



class Consulta(models.Model):
    CHOICES=(
        ("1", "Atendido"),
        ("2", "Aberto"),
        ("3", "Cancelado")
    )
    atendida = models.CharField(max_length=1, choices=CHOICES, blank=False, null=False, default="2")    
    dataConsulta = models.DateField(null=False, blank=False)    
    horaConsulta = models.TimeField(blank=False, null=False)    
    procedimento = models.ForeignKey("Procedimento", on_delete=models.CASCADE,related_name='procedimento_fk')  
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE,related_name='consultas')
    dentista = models.ForeignKey("Dentista", on_delete=models.CASCADE,related_name='consultas2')
    

  



class Dentista(models.Model):    
    crm = models.CharField(max_length=20, null=False, blank=False)
    nome = models.CharField(max_length=100, null=False, blank=False)
    idade = models.CharField(max_length=100, null=False, blank=False)
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nome



    
        
    
