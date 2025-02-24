from django.db import models

class Part(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    revision = models.IntegerField()

    def __str__(self):
        return self.name
    
class Inspection(models.Model):
    part = models.ForeignKey(Part, on_delete=models.PROTECT, related_name="inspections")
    features = models.ManyToManyField("Feature", related_name="inspectionsss")
    date = models.DateField()
    inspector = models.CharField(max_length=100)
    value = models.FloatField()
    result = models.BooleanField()
    notes = models.TextField()
    
    def __str__(self):
        return f"{self.part.name} - {self.date}"

class Feature(models.Model):
    description = models.TextField()
    upper_value = models.FloatField(null=True)
    lower_value = models.FloatField(null=True) 
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name="features")  
    
    def __str__(self):
        return f"{self.description}"



