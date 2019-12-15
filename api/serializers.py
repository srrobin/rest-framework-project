from rest_framework import serializers

from quote.models import QuoteList
from quote.models import QuoteCategory

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteList
        fields = ('__all__')


class QuoteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteCategory
        fields = ('__all__')