
from django.urls import path,include
from api.views import signUp,signIn
urlpatterns = [
   
    path('',signUp),
    path('login/',signIn)

]
