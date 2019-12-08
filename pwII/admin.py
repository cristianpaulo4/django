from django.contrib import admin
from . models import Cliente, Consulta, Dentista, Endereco, Procedimento

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Consulta)
admin.site.register(Dentista)
admin.site.register(Endereco)
admin.site.register(Procedimento)