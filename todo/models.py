from django.db import models

# Create your models here.
class Create(models.Model):
    CHOICES=(
        ('Pending','Pending'),
        ('Completed','Completed')
    )
    STATUS=models.CharField(max_length=100,choices=CHOICES, null=True)
    semester=models.CharField(max_length=100)
    week=models.CharField(max_length=100)
    ToDo=models.CharField(max_length=100)

    def __str__(self):
        return self.semester