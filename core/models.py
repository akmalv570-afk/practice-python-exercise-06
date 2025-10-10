from django.db import models

# Create your models here.
class Dokon(models.Model):
    nomi = models.CharField(max_length=50)
    manzil = models.CharField(max_length=100)

    def __str__(self):
        return f"Nomi:{self.nomi} | Manzil{self.manzil}"
    
class Mahsulot(models.Model):
    nomi = models.CharField(max_length=100)
    narxi = models.IntegerField(null=False)
    dokon = models.ForeignKey(Dokon,on_delete=models.CASCADE,related_name='mahsulotlar')

    def __str__(self):
        return f"Nomi:{self.nomi},Narxi{self.narxi}"
    