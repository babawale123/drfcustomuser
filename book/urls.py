from django.urls import path
from book.views import PostAndGetBook,BookDetailsUpdateAndDelete

urlpatterns = [
    path('',PostAndGetBook.as_view()),
    path('details/<int:pk>/', BookDetailsUpdateAndDelete.as_view()),
]