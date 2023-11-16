from django.urls import path

from store import views

urlpatterns = [
    path("", views.index),
    path("client/", views.client, name="client_form"),
    path("clients/", views.clients, name="clients"),
    path("car-type/", views.car_type, name="car_type_form"),
    path("car-types/", views.car_types, name="car_types"),
    path("car/", views.car, name="car_form"),
    path("cars/", views.cars, name="cars"),
    path("dealer/", views.dealer, name="dealer_form"),
    path("dealers/", views.dealers, name="dealers"),
    path("dealer/<int:pk>", views.dealer_edit, name="dealer_edit"),
    path("order/", views.order, name="order_form"),
    path("quantity/<int:pk>", views.order_edit, name="order_edit"),
    path("quantity/", views.quantity, name="quantity"),
    path("all-orders/", views.all_orders, name="all_orders"),
]
