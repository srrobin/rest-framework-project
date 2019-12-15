from django.contrib import admin

from . models import QuoteCategory
from . models import QuoteList

admin.site.register(QuoteCategory)
admin.site.register(QuoteList)