from django.db import models

# Create your models here.
class BlogPost(models.Model):
    pub_date = models.DateField();
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=999999999999999999);
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title