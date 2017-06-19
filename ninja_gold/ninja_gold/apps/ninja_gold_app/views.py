from django.shortcuts import render, redirect
import random, datetime

def get_time_now():
    return datetime.datetime.now().strftime('(%Y/%m/%d %-I:%M %p)')

# Create your views here.
def index(request):
    try:
        request.session['total_gold']
    except:
        request.session['total_gold'] = 0
        request.session['activities'] = []
    # context {
    #     'total_gold' : request.session['gold']
    #     'activities' : request.session['activities']
    # }
    # return render(request, 'ninja_gold_app/index.html', context)
    return render(request, 'ninja_gold_app/index.html')

def gameplay(request):
    if request.method == 'POST':
        request.session['building'] = request.POST['building']
        if request.session['building'] == 'farm':
            gold_earned = random.randrange(10,20)
            request.session['total_gold'] += gold_earned
            time_str = get_time_now()
            stringout = "Earned " + str(gold_earned) + " from the farm! " + time_str
            html_out = '<p style="color:green;">' + stringout + '</p>'
            request.session['activities'].append(html_out)
        elif request.session['building'] == 'cave':
            gold_earned = random.randrange(5,10)
            request.session['total_gold'] += gold_earned
            time_str = get_time_now()
            stringout = "Earned " + str(gold_earned) + " from the cave! " + time_str
            html_out = '<p style="color:green;">' + stringout + '</p>'
            request.session['activities'].append(html_out)
        elif request.session['building'] == 'house':
            gold_earned = random.randrange(2,5)
            request.session['total_gold'] += gold_earned
            time_str = get_time_now()
            stringout = "Earned " + str(gold_earned) + " from the house! " + time_str
            html_out = '<p style="color:green;">' + stringout + '</p>'
            request.session['activities'].append(html_out)
        elif request.session['building'] == 'casino':
            gold_earned = random.randrange(-50,50)
            request.session['total_gold'] += gold_earned
            time_str = get_time_now()
            if gold_earned < 0:
                stringout = "Lost " + str(gold_earned) + " at the casino! " + time_str
                html_out = '<p style="color:red;">' + stringout + '</p>'
            else:
                stringout = "Earned " + str(gold_earned) + " at the casino! " + time_str
                html_out = '<p style="color:green;">' + stringout + '</p>'
            request.session['activities'].append(html_out)
        # context['activities'] = request.session['activities']
    # return redirect('/', context)
    return redirect('/')

def reset_game(request):
    request.session['total_gold'] = 0
    request.session['activities'] = []
    return redirect('/')
