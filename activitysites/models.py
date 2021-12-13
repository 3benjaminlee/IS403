from django.db import models


# Create your models here.
class activity(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=60)
    location = models.CharField(max_length=30)
    group_size = models.IntegerField(default=1)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    

    class Meta:
        db_table = "activity"

    def __str__(self) :
        return (self.name)