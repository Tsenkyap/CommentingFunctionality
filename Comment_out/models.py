from django.db import models
from django.utils import timezone
# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return ("<name {} ,id {}>".format(self.name,self.id))
    