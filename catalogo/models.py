from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()  # pesos chilenos, sin decimales
    stock = models.PositiveIntegerField(default=0)
    imagen = models.URLField(max_length=300, blank=True)  # link a la foto del producto

    class Meta:
        ordering = ["categoria", "nombre"]

    def __str__(self):
        return f"{self.nombre} (${self.precio})"

    def precio_clp(self):
        # 12990 -> "$12.990"
        return f"${self.precio:,}".replace(",", ".")
