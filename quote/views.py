from django.shortcuts import render
from .models import QuoteList

def quote_list(request):
    quotes = QuoteList.objects.all()
    context ={'quotes':quotes}
    return render(request,'index.html',context)
