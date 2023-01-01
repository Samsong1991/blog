# @Time     : 2023/1/1 9:25 下午
# @Author   : Samsong
# @File     : serializers.py
# @Description:


from rest_framework import serializers
from common.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'avatar', 'email', 'is_active', 'created_at', 'nickname']
