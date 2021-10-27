from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('lagin', views.lagin, name='lagin'),
    path('register', views.register, name='register'),
    path('lout', views.lout, name='lout'),
    path('imageupload', views.imageupload, name='imageupload'),
    path('cat/<int:cid>/', views.catwise, name='catwise'),
    path('aply_story',views.aply_for_story,name='aply_for_story')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
