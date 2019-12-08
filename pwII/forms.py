from django import forms
from . models import Cliente, Endereco, Consulta
from django.contrib.auth.models import User

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ('nome','cpf', 'idade')
			


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class EndForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ('estado', 'cidade', 'bairro', 'logradouro', 'numero')


class ConsultForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ('dataConsulta', 'horaConsulta', 'procedimento', 'dentista', 'atendida')