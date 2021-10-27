from django.db import models

# Create your models here.
class category(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class photos(models.Model) :
    title=models.CharField(max_length=50)
    img=models.TextField(default="")
    ctg=models.ForeignKey(category,on_delete=models.CASCADE)
    disc=models.TextField(default="")

    def __str__(self):
        return self.title



class aply_for_story(models.Model):
    title=models.CharField(max_length=400)
    write=models.TextField(default="")
