from django.db import models
from django.conf import settings

# Create your models here.
class Factory(models.Model):
    name = models.CharField(max_length=15, null=False)
    location = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_factories",
    )
    edited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.location})"
    

class Line(models.Model):
    name = models.CharField(max_length=15, null=False)
    SN = models.CharField(max_length=10, null=False)
    machine_qty = models.SmallIntegerField(null=False)
    product = models.CharField(max_length=25, null=False)
    factory_id = models.ForeignKey(Factory, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_lines",
    )


    def __str__(self):
        return f"{self.name} ({self.SN})"


class Machine(models.Model):
    name = models.CharField(max_length=15, null=False)
    SN = models.CharField(max_length=10, null=False)
    line_id = models.ForeignKey(Line, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_machines",
    )
    


    def __str__(self):
        return f"{self.name} ({self.SN})"
