from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = { 'name': 'Shravan','place':'Earth'}
    return render(request,'index.html', params)


def priya(request):
    return HttpResponse('''<h1>priya</h1><br/><a href="http://127.0.0.1:8000/">Visit Hme</a>''')

def shravan(request):
    return HttpResponse("shravan")

def analize(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(djtext)
    print(removepunc)
    analysed = ""
    for i in djtext:
        if i.isalpha():
            analysed+=i
        elif i==" ":
            analysed = analysed + " "

    params = {'purpose': 'Removed Punctuations','alalyzed_text': analysed}
    return render(request, 'analyze.html',params)
