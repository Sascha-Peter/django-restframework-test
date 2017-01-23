"""Define serializers for the snippet app."""
from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    """Define the serializer for the snippet model."""

    class Meta:
        """Meta definition for SnippetSerializer."""

        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
