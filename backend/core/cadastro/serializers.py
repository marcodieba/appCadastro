from rest_framework import serializers
from .models import Registro


class RegistroSerializer(serializers.ModelSerializer):
    """docstring for RegistroSerializer"""
    # pk = serializers.IntegerField(read_only=True)
    # nome = serializers.CharField(max_length=255)
    # email = serializers.EmailField()
    class Meta:
        model = Registro
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Person` instance, given the validated data.
        :param validated_data:
        """
        return Registro.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """Update and return an existing `Person` instance, given the validated data."""
        instance.nome = validated_data.get('nome', instance.nome)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
