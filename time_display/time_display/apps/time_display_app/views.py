from django.shortcuts import render
import time

# Create your views here.
def index(request):
    request.session['date_display_str'] = time.strftime('%b %d, %Y')
    request.session['time_display_str'] = time.strftime('%l:%M%p')
    return render(request, 'time_display_app/index.html')
