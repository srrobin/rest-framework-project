from django.db import models


class QuoteCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class QuoteList(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=50)
    ctg = models.ForeignKey(QuoteCategory, on_delete=models.CASCADE)


    def __str__(self):
        return self.quote
