from django.shortcuts import render

from book.models import Books
from book.serializer import BooksSerializer


from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework import permissions, authentication

class PostAndGetBook(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self,request):
        book = Books.objects.filter(user=request.user)
        serializer = BooksSerializer(book,many=True)
        return Response(serializer.data)

class BookDetailsUpdateAndDelete(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_babawale(self, pk):
        try:
            return Books.objects.get(pk=pk, user=self.request.user)
        except Books.DoesNotExist:
            return None
    
    def get(self,request, pk):
        book = self.get_babawale(pk)
        if book:
            serializer = BooksSerializer(book)
            return Response(serializer.data)
        return Response({"error": "Note not found"}, status=404)


    def put(self,request,pk):
        book = self.get_babawale(pk)
        if book:
            serializer = BooksSerializer(data=request.data)
            if serializer.is_valid():
                return Response(serializer.data)
            return Response({"error": serializer.errors}, status=404)
        return Response({"error":'book not found'}, status=404)


    def delete(self, request,pk):
        book = self.get_babawale(pk)
        if book:
            book.delete()
            return Response({"Book deleted succesfully"})
        return Response({"error":'book not found'}, status=404)


