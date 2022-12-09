from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Thing(models.Model):
    def validate_quantity(value):
        if value > 100:
            raise ValidationError("This value must be between 0 and 100")
        elif value < 0:
            raise ValidationError("This value must be between 0 and 100")
        else:
            return value
            
    name = models.CharField("name", unique=True, max_length=30, blank=False)
    description = models.TextField("description", max_length=120)
    quantity = models.IntegerField("quantity", max_length=3, blank=False, validators=[validate_quantity])
