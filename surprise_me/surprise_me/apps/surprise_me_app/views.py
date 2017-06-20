from django.shortcuts import render, redirect
import random

VALUES = ['The crow doesn\'t choose the crow life, the crow life chooses the crow.',
    'The good thing about science is that it\'s true whether or not you believe in it.',
    'If you want to make an apple pie from scratch, you must first create the universe.',
    'Theology is ignorance with wings.',
    'The problems we face, did not come down from the heavens. They are made, they are made by bad human decisions, and good human decisions can change them.',
    'It is better to be feared than loved, if you cannot be both.',
    'Imagination is more important than knowledge.',
    'The only thing we have to fear is fear itself.',
    'If you\'re walking down the right path and you\'re willing to keep walking, eventually you\'ll make progress.',
    'Power resides where men believe it resides. It\'s a trick, a shadow on the wall. And a very small man can cast a very large shadow.'
    ]

# Create your views here.
def index(request):
    # print "*"*42
    return render(request, 'surprise_me_app/index.html')

def result(request):
    # print "*"*42
    # print request.method
    if request.method == 'POST':
        try:
            request.session['quote_list']
        except:
            request.session['quote_list'] = VALUES
            print request.session['quote_list']
        random.shuffle(request.session['quote_list'])

        request.session['num_pick'] = request.POST['num_pick']
        # print request.session['num_pick']
        request.session['output_list'] = request.session['quote_list'][:int(request.session['num_pick'])]
        # print request.session['output_list']
        # print request.session['num_pick']
    else:
        return('/')

    return render(request, 'surprise_me_app/result.html')
