from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.HyperlinkedModelSerializer):

    def validate(self, data):
        if data['type'] == 'fiction' and data.get('is_translated', False):
            pass
        elif data['type'] == 'textbook':
            if Book.objects.filter(title=data['title'], author=data['author'], publisher=data.get('publisher'), yearOfRel=data['yearOfRel']).exists():
                raise serializers.ValidationError("Книга с таким названием, автором, годом выпуска и издательством уже существует.")

        return data

    class Meta:
        model = Book
        fields = "__all__"

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"