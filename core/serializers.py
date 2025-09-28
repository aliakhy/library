from rest_framework import serializers

from core.models import MemberUser
from book.serializer import BorrowsSerializer


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberUser
        fields = ['id', 'username', 'email']

