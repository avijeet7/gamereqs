from django.db import models

class Game(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    reqs = models.TextField()
    def __str__(self):
        return str(self.id)+"; "+self.name+"("+self.reqs+")"
