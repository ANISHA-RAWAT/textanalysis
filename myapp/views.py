from django.shortcuts import render

# Create your views here.
# i have created this file-> ani
from django.http import HttpResponse
def home(request) :
    return render(request,"myapp/home.html")
def analyze(request):
    jtext=request.POST.get('text','default')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    removepunc=request.POST.get('removepunc','off')
    extralineremover=request.POST.get('extralineremover','off')
    charc=request.POST.get('charc','off')
    punctuations='''!()-[]{};:'"\,<>./?@#$%&*^_`'''
    if (fullcaps=="on"):
        analyzed=""
        for char in jtext:
                analyzed=analyzed+char.upper()
                parame={'purpose':'changed into uppercase','analysed_text':analyzed}
                jtext=analyzed
        pass            
    if( newlineremover == "on"):
        jtext = request.POST.get('text', 'default')
        analyzed = "".join(jtext.splitlines())

        parame = {
        'purpose': 'Removed New Lines',
        'analysed_text': analyzed
        }
        jtext=analyzed 
        pass     
    if (removepunc=="on"):
        analyzed=""
        for char in jtext:
            if char not in punctuations:
                analyzed=analyzed+char
                parame={'purpose':'Removed Punctuations','analysed_text':analyzed}
        jtext=analyzed
        pass    
    if (extralineremover=="on"):
        analyzed=""
        for index, char in enumerate(jtext):
            if jtext[index] == " "and jtext[index+1] ==" ":
                pass
            else:
                analyzed=analyzed+char
                parame={'purpose':'extra space remover','analysed_text':analyzed}
        jtext=analyzed
        pass    
    if (charc=="on"):
        analyzed= sum(1 for char in jtext if char.isalpha())
        parame={'purpose':'counting characters','analysed_text':analyzed}
        jtext=analyzed
    return render(request,"myapp/analyse.html",parame)
def About(request):
     return render(request,"myapp/about.html")
