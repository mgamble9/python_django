from django.shortcuts import render, redirect
import requests, random
# Create your views here.
word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

def index(request):
    if  not 'attempt_num' in request.session:
        request.session['attempt_num'] = 0
    return render(request, 'random_word_gen_app/index.html')

def random_punch(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print "*"*50
        request.session['attempt_num'] += 1
        word_response = requests.get(word_site)
        WORDS = word_response.content.splitlines()
        # word = random.choice(WORDS)
        request.session['random_word'] = random.choice(WORDS)
        return redirect("/")
    else:
        return redirect("/")
