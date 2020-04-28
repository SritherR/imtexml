from django.db import models

class Hotel(models.Model): 
    name = models.CharField(max_length=50,null=True) 

    
    Image = models.ImageField(upload_to='images/',blank=True,null=True) 
    def __img__(self):
        return self.Image