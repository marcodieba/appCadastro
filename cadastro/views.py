from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader

from .forms import RegistroForm
from .models import Registro
from django.urls import reverse

# from django.views.generic.edit import CreateView
# from django.views.generic import TemplateView
from .serializers import RegistroSerializer

from rest_framework import status, generics
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import authentication, permissions

# def index(request):
    # busca = Registro.objects.order_by('-nome')[:5]
    # output = ', '.join([q.nome for q in busca])
    # template = loader.get_template('index.html')
    # context = {
    #     'busca': busca,
    # }

# class RecordCreate(CreateView):
#     form_class = RegistroForm
#     template_name = 'index.html'

#     def get_success_url(self):
#         return reverse('record_form_success')
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
            return HttpResponseRedirect('/tanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistroForm()

    return render(request, 'index.html', {'form': form})
    # return HttpResponse(template.render(context, request))

class PersonList(APIView):
    """
    List all persons, or create a new person.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'busca.html'

    def get(self, request):
        persons = Registro.objects.all()
        
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
