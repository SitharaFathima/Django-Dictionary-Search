from django.db import models


class WordofDay(models.Model):
    word=models.CharField(max_length=255)
    definition=models.TextField()
    
    def __str__(self):
        return self.word

