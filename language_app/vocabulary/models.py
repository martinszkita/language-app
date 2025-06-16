from django.db import models

class Language(models.Model):
    name=models.CharField(max_length=30, unique=True)
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

# Create your models here.
class Word(models.Model):
    name=models.CharField(max_length=30)
    language=models.ForeignKey(Language, on_delete=models.CASCADE)
    polish_translation=models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} - {self.language} - {self.polish_translation}"
