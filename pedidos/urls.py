from django.urls import path

from . import views

app_name="pedido"

urlpatterns = [
    path('', views.procesar_pedido, name="procesar_pedido"),
    # path("enviar/", views.procesar_pedido, name="enviar"),
]

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)