from django.db import models
from django.contrib.auth.models import User
from sklearn.ensemble import RandomForestClassifier
import joblib

class Crop(models.Model):
    Area = models.CharField(max_length=1000, null = True)
    Taken_at = models.DateTimeField(auto_now_add = True)
    Nitrogen = models.PositiveIntegerField(null = True)
    Phosphorus = models.PositiveIntegerField(null = True)
    Potassium = models.PositiveIntegerField(null = True)
    Temperature = models.CharField(max_length =1000, null=True)
    Humidity = models.CharField(max_length=1000,null = True)
    Soil_pH = models.CharField(max_length=1000,null = True)
    Rainfall = models.CharField(max_length=1000,null = True)
    Crop_supported = models.CharField(max_length=1000, blank = True)
    Action = models.CharField(max_length=1000,null = True)
    
    def save(self, *args, **kwargs):
        ml_model = joblib.load('./ml_model/crop_recomender.joblib')
        self.Crop_supported = ml_model.predict([[self.Nitrogen, self.Phosphorus, self.Potassium, self.Temperature, self.Humidity, self.Soil_pH, self.Rainfall]])
        return super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-Taken_at']

    def __str__(self):
        return self.Area
