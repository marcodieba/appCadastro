from django.conf.urls import url
from django.contrib import admin    
from cadastro import views
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
    # url(r'^$', views.RecordCreate, name='RecordCreate'),
    url(r'^$', views.index, name='index'),
    # url(r'^list/', views.NomeView.as_view()),
    url(r'^persons/$', views.PersonList.as_view(), name='persons'),
    url(r'^persons/(?P<nome>[\w \-]+)/$', views.PersonDetail.as_view()),
    # url(r'^busca/', views.manage_cadastro, name='busca'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
