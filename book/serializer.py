from rest_framework import serializers
from book.models import Books

class BooksSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta(object):
        model = Books
        fields = '__all__'