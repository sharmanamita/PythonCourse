from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello, World!")

def greet(request):
    x = 25
    y = 35
    sum = x+y
    print("The sum is:", sum)
    return render(request, 'greet.html', {'name': 'Namita'})