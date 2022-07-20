from django.shortcuts import render, redirect
from .models import Food, Consume
# Create your views here.

def index(request):

    if request.user.is_authenticated:
        if request.method == "POST":
            food_consumed = request.POST['food_consumed']
            consume = Food.objects.get(name=food_consumed)
            user = request.user
            consume = Consume(user=user, food_consumed=consume)
            consume.save()
            foods = Food.objects.all()
        else:
            foods = Food.objects.all()
        consumed_food = Consume.objects.filter().first()
        return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food})
        return render(request, 'myapp/index.html')
    else:
        return render(request, 'myapp/index.html')

def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.user.is_authenticated:
        if request.method == "POST":
            consumed_food.delete()
            return redirect('/')
        return render(request, 'myapp/delete.html')
    else:
        return render(request, 'myapp/delete.html')
