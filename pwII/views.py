from django.shortcuts import render
from .forms import ClienteForm, UserForm, EndForm, ConsultForm
from django.shortcuts import redirect
from . models import Cliente, Endereco, Consulta, Procedimento, Dentista
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.dateparse import parse_date



# Create your views here.

def index(request):
	return render(request,'pwII/index.html',{'msg':False})



def login(request): 	
    return render(request, 'pwII/login.html')


def dash(request):  
    form = ConsultForm()  
    user = request.POST.get('usuario') 
    senha = request.POST.get('senha')
    if request.method=="POST":        
        user = authenticate(request,username=user, password=senha)     
        if user is not None:   
            cliente = Cliente.objects.get(user = user)    
            list_consulta = "/list_consulta/"+str(cliente.pk) 
            return redirect(list_consulta) 
        else:
            return render(request, 'pwII/login.html', {'msg':True}) 
    
    return render(request, 'pwII/login.html',{'msg':False})
        
    
    

def confimar_consulta(request):
    cliente = Cliente.objects.get(pk=request.POST['cliete_id'])
    dataConsulta =  request.POST['dataConsulta']
    horaConsulta =  request.POST['horaConsulta']
    procedimento =  Procedimento.objects.get(pk= request.POST['procedimento'])
    dentista = Dentista.objects.get(pk=request.POST['dentista'])
    return render(request, 'pwII/confimar_consulta.html',{'user':cliente, 'dataConsulta':dataConsulta, 'horaConsulta':horaConsulta, 'procedimento':procedimento, 'dentista':dentista })
    
def list_consulta(request, pk):
    usuario= Cliente.objects.get(pk=pk)
    consulta = Consulta.objects.all().filter(cliente=pk, atendida="2") 
    return render(request, 'pwII/list_consulta.html',{'user':usuario, 'consulta':consulta})
    
def salvar_consulta(request): 
    data = parse_date(request.POST.get('dataConsulta'))    
    cliente = Cliente.objects.get(id=request.POST.get('cliete_id'))
    procedimento =Procedimento.objects.get(pk=request.POST['procedimento'])
    dentista = Dentista.objects.get(pk = request.POST.get('dentista'))    
    consulta = Consulta.objects.create(cliente=cliente, procedimento=procedimento, dentista=dentista,dataConsulta=data,horaConsulta=request.POST.get('horaConsulta'), atendida = "2")
    consulta.save()
    form = ConsultForm() 
    
    return render(request, 'pwII/marcar.html',{'user':cliente, 'form':form})

def marcar(request, pk):     
    form = ConsultForm() 
    usuario= Cliente.objects.get(pk=pk)
    return render(request, 'pwII/marcar.html', {'form':form, 'user':usuario})


def historico(request, pk):
    cliente= Cliente.objects.get(pk=pk) 
    consulta = Consulta.objects.all().filter(cliente=pk) 
    return render(request, 'pwII/historico.html', {'user':cliente, 'consulta':consulta,})


def minha_conta(request):
	return render(request, 'pwII/minha_conta.html')


def cadastrar(request):  
    if request.method == "POST":
        usuario = User.objects.get(id=request.POST['user'])
        #form = ClienteForm()     
        cliente = Cliente.objects.create(nome = request.POST.get('nome'), cpf = request.POST.get('cpf'), idade = request.POST.get('idade'), user = usuario)           
        cliente.save()
        form = EndForm()        
        if request.method == "POST":return render(request, 'pwII/endereco.html', {'form':form, 'user':usuario})                        
    
       

def cadUser(request):
    form = UserForm()
    if request.method=="POST":
        user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'),request.POST.get('password'))
        user.is_staff = True
        user.save()
        form = ClienteForm()	
        return render(request, 'pwII/cadastre.html', {'form':form, 'user':user})  
    
    return render(request, 'pwII/usuario.html', {'form':form})



def cancelar_consulta(request, pk):
    consulta = Consulta.objects.get(id = pk)
    consulta.atendida = "3"
    consulta.save()   
    print(consulta.cliente.pk)
    list_consulta = "/list_consulta/"+str(consulta.cliente.pk) 
    return redirect(list_consulta)    
  
    

def cadEnd(request):
    if request.method=="POST":
        usuario = User.objects.get(id=request.POST['user'])
        end = Endereco.objects.create(estado = request.POST.get('estado'), cidade = request.POST.get('cidade'), bairro = request.POST.get('bairro'), logradouro = request.POST.get('logradouro'), numero = request.POST.get('numero'))
        end.is_staff = True
        end.save()
        cliente = Cliente.objects.get(user = usuario)
        cliente.endereco = end
        cliente.save()      
        
        return render(request, 'pwII/login.html')
        
    
def logout_view(request):
    logout(request)
    return render(request, 'pwII/login.html')


def alterar_consulta(request, pk):
    form = ConsultForm()     
    consulta = Consulta.objects.get(pk = pk)    
    cliente = Cliente.objects.get(pk=consulta.cliente.pk)
    proce = Procedimento.objects.all()
    dentista = Dentista.objects.all()
            

    return render(request, 'pwII/alterar_consulta.html', {'user':cliente, 'consulta':consulta, 'form':form, 'data':str(consulta.dataConsulta),'proce':proce,'dentista':dentista, 'hora':str(consulta.horaConsulta)})
   
    

def confirmar_alteracoes(request):   
    consulta = Consulta.objects.get(pk = request.POST['consulta_id'])    
    consulta.dataConsulta = request.POST['dataConsulta']
    consulta.horaConsulta = request.POST['horaConsulta']    

    dentista = Dentista.objects.get(pk = request.POST['dentista'])
    consulta.dentista =  dentista
    procedimento = Procedimento.objects.get(pk= request.POST['procedimento'])
    consulta.procedimento =  procedimento
    consulta.save()   
    list_consulta = "/list_consulta/"+str(consulta.cliente.pk) 
    return redirect(list_consulta) 
    

    
def alterar_meus_dados(request,pk):        
    cliente = Cliente.objects.get(pk = pk)  
    user_dados_cliente = Cliente.objects.get(id=pk)
    return render(request, 'pwII/alterar_meus_dados.html', {'user_dados_cliente':user_dados_cliente,'user':cliente})


def salvar_meus_dados(request):
    cliente = Cliente.objects.get(pk=request.POST['cliete_id'])
    if request.POST['username']!=cliente.user.username or request.POST['senha']!=cliente.user.password:
        user = User.objects.get(pk = cliente.user.pk)
        user.username = request.POST['username']
        user.password = request.POST['senha']
        user.save()
        logout(request)
        return render(request, 'pwII/login.html')
           
    cliente.nome = request.POST['nome']
    cliente.cpf = request.POST['cpf']
    cliente.idade = request.POST['idade']
    end = Endereco.objects.get(pk = cliente.endereco.pk)
    end.estado = request.POST['estado']
    end.cidade = request.POST['cidade']
    end.logradouro = request.POST['logradouro']
    end.numero = request.POST['numero']
    end.save()
    cliente.save()      

    consulta = Consulta.objects.all().filter(cliente=cliente.pk, atendida="2") 
    return render(request, 'pwII/list_consulta.html',{'user':cliente, 'consulta':consulta})
   

def excluir_historico(request, pk):
    consulta = Consulta.objects.get(pk = pk)
    id_cliente = consulta.cliente.pk
    cliente = Cliente.objects.get(pk=id_cliente)
    consulta.delete() 
    return render( request, 'pwII/historico.html',{'user':cliente})

 

    