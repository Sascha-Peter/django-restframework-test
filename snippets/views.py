"""Define views for the restful api."""
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class SnippetList(APIView):
    """Class based implementation of the snippet list view."""

    def get(self, request, format=None):
        """Implement GET method for snippet list.

        Arguments:
            request -- HTTP request to snippet list view
            format -- string, format of response
        """
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Implement POST method for snippet list.

        Arguments:
            request -- HTTP requst for snippet list view
            format -- string, format of response
        """
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """Class based implementation of the snippet detail view."""

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
