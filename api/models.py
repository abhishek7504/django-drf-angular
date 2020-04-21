from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator



class Movie(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField(max_length = 360)

    def __str__(self):
        return self.title



class Rating(models.Model):
    movie = models.ForeignKey(Movie,on_delete = models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True,blank=True)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('user','movie'),)
        index_together = (('user','movie'),)

    def __str__(self):
        return f"{self.user} has given {self.stars} stars to {self.movie}"
