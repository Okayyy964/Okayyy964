from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.main,name='main'),
    url(r'^check/',views.check,name='check'),
    url(r'^generate/',views.generate,name='generate'),
    url(r'^post_check/',views.post_check,name='post_check'),
    url(r'^post_generate/',views.post_generate,name='post_generate'),

]
