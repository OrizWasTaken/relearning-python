from django.shortcuts import render
from .models import Pizza

def index(request):
    """The home page for pizzas."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Show all orders."""
    pizzas = Pizza.objects.order_by('date_added')
    content = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', content)

def pizza(request, pizza_id):
    """Show a single pizza and all its toppings."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.toppings_set.all()
    content = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', content)