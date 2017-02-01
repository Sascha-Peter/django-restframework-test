"""Define serializers for the snippet app."""
from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    """Define the serializer for the snippet model."""

    class Meta:
        """Meta definition for SnippetSerializer."""

        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.ModelSerializer):
    """Define the serializer for the user model."""

    snippets = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Snippet.object.all()
    )

    class Meta:
        """User serializer meta definition."""

        model = User
        fields = ('id', 'username', 'snippets')
