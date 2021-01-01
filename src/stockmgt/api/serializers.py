from rest_framework import serializers
from stockmgt.models import Stock

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields=['category', 'item_name' , 'quantity']

