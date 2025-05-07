from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from DjangoProject.model_test.models import Book, Author


class BookSerializer(ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('title', )

    # def to_representation(self, instance):
    #     return {
    #         'title': instance.title,
    #         'author': instance.author.name,
    #     }

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'author': instance.name,
            'books': BookSerializer(instance.book_set.first()).data
        }


