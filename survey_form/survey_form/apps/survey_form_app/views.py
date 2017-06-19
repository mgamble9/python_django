from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'survey_form_app/index.html')

def process(request):
    if not 'num_results' in request.session:
        request.session['num_results'] = 0
    if request.method == 'POST':
        request.session['num_results'] += 1
        print request.POST
        request.session['name'] = request.POST['full_name']
        request.session['city_location'] = request.POST['city_location']
        request.session['fave_language'] = request.POST['fave_language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        return redirect("/")

def result(request):
    return render(request, 'survey_form_app/result.html')
