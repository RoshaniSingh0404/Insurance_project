from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    emp_id = models.PositiveBigIntegerField()

    def __str__(self):
        return self.first_name

