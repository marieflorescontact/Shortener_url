from django.db import models

# Create your models here.
'''
Url qrcode model
'''


# Create your models here.

class Qrcod(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    times_followed = models.PositiveIntegerField(default=0)

    text = models.URLField()

    qr_code = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.text}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
