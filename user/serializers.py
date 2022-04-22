import json

from rest_framework import serializers

from user.models import Users



class UserSerializer(serializers.ModelSerializer):
    user_type_display = serializers.CharField(source='get_user_type_display',read_only=True)

    # TODO 需要将密码加密
    def create(self, validated_data):
        username = validated_data.get('username', None)
        password = validated_data.get('password', None)

        # 用户名密码不能为空 用户名不能重复 密码不能少于六位
        if not username:
            msg = {'username':'用户名不能为空'}
            raise serializers.ValidationError(msg)
        elif not password:
            msg = {'password':'密码不能为空'}
            raise serializers.ValidationError(msg)
        elif Users.objects.filter(username=username).exists():
            msg = {'username':'用户名已存在'}
            raise serializers.ValidationError(msg)
        elif len(password) < 6:
            msg = {'password':'密码不能少于六位'}
            raise serializers.ValidationError(msg)

        return Users.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        username = validated_data.get('usernmae', None)
        password = validated_data.get('password', None)

        if username and Users.objects.filter(usernmae=username).exists():
            msg = {'username':'用户名已存在'}
            raise serializers.ValidationError(msg)
        elif password and len(password) < 6:
            msg = {'password':'密码不能少于六位'}
            raise serializers.ValidationError(msg)
        
        return super(UserSerializer, self).update(instance, validated_data)

    class Meta:
        model = Users
        fields = '__all__'