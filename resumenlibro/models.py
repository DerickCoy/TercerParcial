from django.db import models

class Post(models.Model):
    autor = models.CharField(max_length=200)
    autor_del_libro= models.CharField(max_length=200)
    libro = models.CharField(max_length=300)
    resumen  = models.TextField()
    
    def __str__(self):
        return self.autor