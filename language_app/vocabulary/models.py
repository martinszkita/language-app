from django.db import models

class Language(models.Model):
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.name}"

# Create your models here.
class Word(models.Model):
    name=models.CharField(max_length=30)
    language=models.ForeignKey(Language, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.language}"
