from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'disappearing_ninjas_app/index.html')

def ninjas(request):
    context = {
        'ninja_img' : 'tmnt.png'
    }
    print context
    return render(request, "disappearing_ninjas_app/ninja.html", context)

def ninjas_color(request, ninja_color):
    if ninja_color == "red":
        ninja_img = "raphael.jpg"
    elif ninja_color == "blue":
        ninja_img = "leonardo.jpg"
    elif ninja_color == "purple":
        ninja_img = "donatello.jpg"
    elif ninja_color == "orange":
        ninja_img = "michelangelo.jpg"
    else:
        ninja_img = "notapril.jpg"
    # print "*"*42
    # print ninja_color
    # print "*"*42
    context = {
        'ninja_img' : ninja_img
    }
    print context
    return render(request, "disappearing_ninjas_app/ninja.html", context)
