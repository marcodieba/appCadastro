from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .serializers import RegistroSerializer
from .forms import RegistroForm
from .models import Registro
from rest_framework import status, generics
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import authentication, permissions



@login_required
def menu(request):
    return render(request, 'menu.html')    

@login_required
def index(request):
    # data = {}
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        # data['nome'] = request.POST.get('nome')
        # print(data)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/persons/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistroForm()

    return render(request, 'formulario.html', {'form': form})
    # return HttpResponse(template.render(context, request))
def busca(request):
    pass
@login_required    
def person_edit(request, pk):

    post = get_object_or_404(Registro, pk=pk)
    
    if request.method == "POST":
        form = RegistroForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect('/persons/')
    else:
        form = RegistroForm(instance=post)
    return render(request, 'formulario.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

class PersonList(APIView):
    """
    List all persons, or create a new person.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'busca.html'

    def get(self, request):
        persons = Registro.objects.all()
        # form = 
        
        return Response({'content':persons})

    # def post(self, request, format=None):
    #     serializer = RegistroSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PersonDetail(APIView):
    """
    Retrieve, update or delete a person instance.
    """

    def get_object(self, nome):
        try:
            return Registro.objects.get(nome=nome)
        except Registro.DoesNotExist:
            raise Http404

    def get(self, request, nome, format=None):
        person = self.get_object(nome)
        serializer = RegistroSerializer(person)
        return Response(serializer.data)

    def put(self, request, nome, format=None):
        person = self.get_object(nome)
        serializer = RegistroSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, nome, format=None):
        person = self.get_object(nome)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
