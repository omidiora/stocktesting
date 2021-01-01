from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from stockmgt.api.serializers import ListSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from stockmgt.models import Stock



class ListViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class =ListSerializer
    queryset = Stock.objects.all()