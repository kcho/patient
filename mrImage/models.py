from django.db import models

# Create your models here.

class MRIMAGE(models.Model):
    hospitalID= models.CharField(max_length=8)
    image_file = models.ImageField(upload_to='static_files/uploaded/%Y/%m/%d')
    description = models.TextField(max_length=400, blank = True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def delete(self, *args, **kwargs):
        self.image_file.delete()
        super(MRIMAGE, self).delete(*args, **kwargs)
