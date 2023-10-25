from django.db import models

# Create your models here.


class Contacto(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    mensaje_cliente = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        db_table = "contactos"
        ordering = ['-created_at']
