"""Define views for the restful api."""
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User


class SnippetList(generics.ListCreateAPIView):
    """Class based implementation of the snippet list view."""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        """Overwrite perform_create to add user to the snippet."""
        serializer.save(owner=self.request.user)


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """Class based implementation of the snippet detail view."""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        """Implement GET method for snippet detail view.

        Arguments:
            request -- HTTP request
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Implement PUT method for snippet detail view.

        Arguments:
            request -- HTTP request
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Implement DELETE method for snippet detail view.

        Arguments:
            request -- HTTP request
        """
        return self.destroy(request, *args, **kwargs)


class UserList(generics.ListAPIView):
    """Class based implementation of the user list view."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """Class based implementation of the user detail view."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
