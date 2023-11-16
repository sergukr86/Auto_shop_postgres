from django.http import HttpResponse
from django.shortcuts import render, redirect

from store.forms import *
from store.models import CarType


def index(request):
    return HttpResponse("Hello from Heroku!")


# form for creating new clients
def client(request):
    if request.method != "POST":
        form = ClientForm()
        return render(request, "client.html", {"form": form})
    form = ClientForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("clients")

    return render(request, "client.html", {"form": form})


def clients(request):
    all_clients = Client.objects.all()
    return render(request, "clients.html", context={"all_clients": all_clients})


def car_type(request):
    if request.method != "POST":
        form = CarTypeForm()
        return render(request, "car-type.html", {"form": form})
    form = CarTypeForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("car_types")

    return render(request, "car-type.html", {"form": form})


def car_types(request):
    types = CarType.objects.all()
    return render(request, "car-types.html", context={"types": types})


def car(request):
    if request.method != "POST":
        form = CarForm()
        return render(request, "car.html", {"form": form})
    form = CarForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("cars")

    return render(request, "car.html", {"form": form})


def cars(request):
    auto = Car.objects.all()
    return render(request, "cars.html", context={"cars": auto})


def dealer(request):
    if request.method != "POST":
        form = DealershipForm()
        return render(request, "dealer.html", {"form": form})
    form = DealershipForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        clients = form.cleaned_data["clients"]
        available_car_types = form.cleaned_data["available_car_types"]

        dealership = Dealership.objects.create(
            name=name,
        )
        dealership.clients.set(clients)
        dealership.available_car_types.set(available_car_types)
        return redirect("dealer_edit", pk=dealership.pk)

    return render(request, "dealer.html", {"form": form})


def dealer_edit(request, pk):
    deal = Dealership.objects.get(pk=pk)
    if request.method == "GET":
        form = DealershipForm(instance=deal)
        return render(request, "dealer_edit.html", {"form": form})
    form = DealershipForm(request.POST, instance=deal)
    if form.is_valid():
        form.save()
        return redirect("dealers")

    return render(request, "dealer_edit.html", {"form": form})


def dealers(request):
    deal = Dealership.objects.all()
    return render(request, "dealers.html", context={"dealers": deal})


def order(request):
    if request.method != "POST":
        form = OrderForm()
        return render(request, "order.html", context={"form": form})
    form = OrderForm(request.POST)
    if form.is_valid():
        client = form.cleaned_data["client"]
        dealership = form.cleaned_data["dealership"]
        cars = form.cleaned_data["car"]
        Order.objects.create(client=client, dealership=dealership, car=cars[0])
        return redirect("quantity")
    return render(request, "order.html", context={"form": form})


def quantity(request):
    if request.method != "POST":
        form = QuantityForm()
        return render(request, "quantity.html", context={"form": form})
    form = QuantityForm(request.POST)
    if form.is_valid():
        form.save()

        return redirect("all_orders")
    return render(request, "order.html", context={"form": form})


def order_edit(request, pk):
    order_q = OrderQuantity.objects.get(pk=pk)
    order = Order.objects.get(id=order_q.order.id)
    car = Car.objects.get(id=order.car_id)
    if request.method == "GET":
        form = QuantityForm(instance=order_q)
        return render(request, "order_edit.html", {"form": form})
    form = QuantityForm(request.POST, instance=order_q)
    if form.is_valid():
        if car.blocked_by_order_id:
            car.unblock()
        else:
            car.block(order)
        if order_q.is_paid == 1:
            car.sell()
        form.save()
        return redirect("all_orders")

    return render(request, "order_edit.html", {"form": form})


def all_orders(request):
    orders = OrderQuantity.objects.all()
    return render(request, "all-orders.html", context={"all_orders": orders})
