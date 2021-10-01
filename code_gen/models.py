from django.db import models
import qrcode as qr
# Create your models here.
class code_data(models.Model):
    name=models.CharField(max_length=50 , default="Undefined")
    data = models.CharField(max_length=50000)
    image = models.FileField(upload_to='code_gen/images', null=True, verbose_name="")
    def __str__(self):
        return self.name