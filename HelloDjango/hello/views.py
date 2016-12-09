from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response

def search(request):
    return render_to_response('search.html')
def result(request):
    question = request.GET['q']
    ansa = request.GET['a']
    ansb = request.GET['b']
    ansc = request.GET['c']
    ansd = request.GET['d']
    for index, line in enumerate(open('C:/workspace/MyPythonWorkspace/HelloDjango/hello/final.txt')):
        lst = line.split('\t')
        if(lst[0]==question):
            path = lst[2].split(',')
            id = lst[1]
       # lst = line.strip('\n').strip(',').split('\t')
    for index, line in enumerate(open('C:/workspace/MyPythonWorkspace/HelloDjango/hello/count_file.txt')):
        lst = line.split(',')
        if(lst[0]==question):
            tfa = lst[1]
            tfb = lst[2]
            tfc = lst[3]
            tfd = lst[4]
    count = 0
    if(tfa>=count):
        answer = 'A'
        count = tfa
    if(tfb>=count):
        answer = 'B'
        count = tfb
    if(tfc>=count):
        answer = 'C'
        count = tfc
    if(tfd>=count):
        answer = 'D'
        count = tfd

    message = {'question':question,'ansa':ansa,'ansb':ansb,'ansc':ansc,'ansd':ansd,'path':path,'tfa':tfa,'tfb':tfb,'tfc':tfc,'tfd':tfd,'answer':answer}
    return render_to_response('result.html',{'message':message})
   # if not key :
   #     message = 'input what you search'
   #     return render_to_response('result.html',{'message':message})
   # else :
   #     message = 'the CorrectAnswer is  C'
   #     return render_to_response('result.html',{'message':message})