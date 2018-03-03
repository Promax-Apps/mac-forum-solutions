from django.contrib import admin
from django.urls import path
from .views import hello, say_hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
    path('index/', hello),
    path('SayHello/<str:name>', say_hello)
]
