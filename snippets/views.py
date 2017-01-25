"""Define views for the restful api."""
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """Class based implementation of the snippet list view."""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        """Implement GET method for snippet list.

        Arguments:
            request -- HTTP request to snippet list view
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Implement POST method for snippet list.

        Arguments:
            request -- HTTP requst for snippet list view
        """
        return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generic.GenericAPIView):
    """Class based implementation of the snippet detail view."""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get_object(self, pk):
        """Implement get of 404.

        Arguments:
            pk -- int, identifier of snippet to get
        """
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """Implement GET method for snippet detail view.

        Arguments:
            request -- HTTP request
            pk -- int, identifier of snippet to get
            format -- string, format of response
        """
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """Implement PUT method for snippet detail view.

        Arguments:
            request -- HTTP request
            pk -- int, identifier of snippet to update
            format -- string, format of response
        """
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """Implement DELETE method for snippet detail view.

        Arguments:
            request -- HTTP request
            pk -- int, identifier of snippet to delete
            format -- string, format of response
        """
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
