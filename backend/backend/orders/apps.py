from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "backend.orders"
    label = "orders"
    verbose_name = "Order Purchases"
