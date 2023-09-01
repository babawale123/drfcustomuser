
from django.urls import path,include
from api.views import signUp,signIn,TestApi
urlpatterns = [
   
    path('',signUp),
    path('login/',signIn),
    path('test/',TestApi.as_view())

]
