from django.shortcuts import render, HttpResponse

# def index(request):
#     response = 'YOOOOOO!'
#     return HttpResponse(response)

def index(request):
  print "helloooooooo"
  return render(request, 'hello_world_app/index.html')


# Create your views here.
