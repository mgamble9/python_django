from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print "*"*42
    return render(request, 'landscapes_app/index.html')

def img_result(request, id):
    # print id
    id_int = int(id)
    if (id_int < 1 or id_int > 50):
        return redirect('/')
    if id_int < 51:
        img_displayed = 'tropical.jpg'
    if id_int < 41:
        img_displayed = 'vineyard.jpg'
    if id_int < 31:
        img_displayed = 'forest.jpg'
    if id_int < 21:
        img_displayed = 'desert.jpg'
    if id_int < 11:
        img_displayed = 'snow.jpg'
    context = {
        'img_displayed' : img_displayed
    }
    print context
    return render(request, 'landscapes_app/result.html', context)
