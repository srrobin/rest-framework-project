from rest_framework import generics,permissions

from quote.models import QuoteList
from quote.models import QuoteCategory

from .serializers import QuoteSerializer
from .serializers import QuoteCategorySerializer


class QuoteAPIView(generics.ListAPIView):
    permission_classes =(permissions.IsAuthenticated,)
    queryset = QuoteList.objects.all()
    serializer_class = QuoteSerializer



class QuoteCategoryAPIView(generics.ListAPIView):
    queryset = QuoteCategory.objects.all()
    serializer_class = QuoteCategorySerializer


class QuoteAPIDetailView( generics.RetrieveUpdateDestroyAPIView):
    queryset = QuoteList.objects.all()
    serializer_class = QuoteSerializer

class QuoteAPINewView(generics.ListCreateAPIView):
    queryset = QuoteList.objects.all().order_by('-id')[:1]
    serializer_class = QuoteSerializer