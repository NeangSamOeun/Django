from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}({self.id})"

class product(models.Model):
    name = models.CharField(max_length=30)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    volume = models.CharField(max_length=10)
    description = models.CharField(max_length=255) 
    image = models.CharField(max_length=300)
 
    def __str__(self):
        return f"{self.name} ({self.id})"
    