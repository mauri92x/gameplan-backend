# apps/users/serializers.py

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Validar las credenciales y obtener los tokens
        data = super().validate(attrs)

        # Asegurarse de que los tokens estén en la respuesta
        tokens = {
            'access': data.get('access'),
            'refresh': data.get('refresh'),
        }

        # Añadir los datos del usuario a la respuesta
        user_serializer = UserSerializer(self.user)
        data['user'] = user_serializer.data
        data['permissions'] = []  # Ajusta según tus necesidades

        # Incluir los tokens en la respuesta
        data.update(tokens)

        return data