from django.shortcuts import render
from .models import Producto


def inicio(request):
    productos = Producto.objects.all()
    categorias = Producto.objects.values_list("categoria", flat=True).distinct().order_by("categoria")

    categoria = request.GET.get("categoria", "")
    busqueda = request.GET.get("q", "").strip()

    if categoria:
        productos = productos.filter(categoria=categoria)
    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)

    contexto = {
        "productos": productos,
        "categorias": categorias,
        "categoria_actual": categoria,
        "busqueda": busqueda,
    }
    return render(request, "catalogo/index.html", contexto)