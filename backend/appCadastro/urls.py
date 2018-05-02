from django.conf.urls import url
from django.contrib import admin    
from backend.core.cadastro import views
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
# from .views import RecordCreate
# from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'list', views.NomeView, base_name='list')
# # router.register(r'person/food', views.PersonViewSet, 'Person')
# urlpatterns = router.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.menu, name='menu'),
    url(r'^formulario$', views.index, name='cadastro'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^persons/$', views.PersonList.as_view(), name='persons'),
    url(r'^persons/(?P<nome>[\w \-]+)/$', views.PersonDetail.as_view()),
    url(r'^persons/(?P<pk>\d+)/edit/$', views.person_edit, name='persons'),
    # url(r'^busca/', views.manage_cadastro, name='busca'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
