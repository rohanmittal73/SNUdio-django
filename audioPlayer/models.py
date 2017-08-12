from django.db import models


# Create your models here.
class AudioFile(models.Model):
    date = models.DateField()
    time = models.TimeField(default='19:00')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.FileField()
    audio = models.FileField(blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.date.__str__()+" : "+self.title


class Member(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    profile_image = models.FileField()

    def __str__(self):
        return self.name+" - "+self.designation

