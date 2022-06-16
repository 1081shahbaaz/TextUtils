# I have created this file - Shahbaaz
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render (request, 'index.html')


def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount','off')
    if removepunc == 'on':
        punctuations = '''!()-[]{;}:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char 
    

        params = {'purpose':'Remove Puncutations','analyzed_text': analyzed}
        djtext = analyzed
    

    if fullcaps == 'on':
        analyzed = djtext.upper()
        params = {'purpose':'Changed to UpperCase','analyzed_text': analyzed}
    
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed = analyzed+char 
        params = {'purpose':'Remove New lines','analyzed_text': analyzed}
   
        djtext = analyzed
    if extraspaceremover == 'on':
        analyzed = ''
        for index,char in enumerate(djtext):
            if not(djtext[index] ==' ' and djtext[index+1] == ' '):
                analyzed = analyzed+char
                
        params = {'purpose':'Remove Extra Spaces','analyzed_text': analyzed}
   
        djtext = analyzed
    if charcount == 'on':
        analyzed = 0
        for i in djtext:
            analyzed+=1
                
        params = {'purpose':'Character Counter','analyzed_text': analyzed}
        
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")
    
    return render(request, 'analyze.html',params)




