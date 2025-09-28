from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Borrow,Book
User=get_user_model()


class BorrowsSerializer(serializers.ModelSerializer):
    book_title=serializers.CharField(source='book.title')

    class Meta:
        model = Borrow
        fields=('book_title','borrow_at','return_due')

    def create(self,validated_data ):
        try:
            book_title = validated_data.get('book', {}).get('title')
            book=Book.objects.get(title=book_title)
            user_id=self.context['member_pk']
            user=User.objects.get(pk=user_id)

            return Borrow.objects.create(
                user=user,
                book=book,
                return_due=validated_data.get('return_due')
            )
        except Book.DoesNotExist:
            pass