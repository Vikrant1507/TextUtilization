#i have created the file Vikky

from django.http import HttpResponse
from django.shortcuts import render

#code before pipeling
#code for pipeline
def index(request):
    # params={'name':'Vikky','Place':'Bangalore'}
    return render(request,'index.html' )
    # return HttpResponse("Hello Vikky")
    # return HttpResponse('''Hello World i am Vikky <br>
    #  <a href="http://127.0.0.1:8000/removepunc">RemovePunc Link Is Here</a><br>''')


def about(request):
    return HttpResponse('''<h1>Vikky</h1> \n <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Code With Vikky</a>''')

# def removepunc(request):
#     #Get the text
#     djtext = request.GET.get('text','default')
#     print(djtext)
#     #Analyze the text
#     return HttpResponse("Remove <a href ='/'back</a>")

# def capitalizefirst(request):
#     return HttpResponse("cap first<a href='/'>back</a>")
#
# def newlineremover(request):
#     return HttpResponse("newline remover<a href='/'>back</a>")
#
# def spaceremover(request):
#     return HttpResponse("spaceremover <a href='/'>back</a>")
#
# def charcount(request):
#     return HttpResponse("char count<a href='/'>back</a>")



def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')

    #check checkboxvalues
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineRemover = request.POST.get('newlineRemover','off')
    ExtraSpaceRemover = request.POST.get('ExtraSpaceRemover','off')
    CharacterCounter = request.POST.get('CharacterCounter','off')
    # print(removepunc)
    # print(djtext)

    # Analyze the text
    #checkbox is on
    if removepunc == 'on':
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed + char
        params={'Purpose':'remove punctuations','analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(fullcaps == 'on'):
        analyzed =""
        for char in djtext:
            analyzed = analyzed +char.upper()
        params = {'Purpose': 'change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(newlineRemover == 'on'):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                # in network to transport new line character we need \n and \r
                analyzed = analyzed + char
        params = {'Purpose': 'Remove Newline', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(ExtraSpaceRemover == 'on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'Purpose': 'ExtraSpaceRemover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(CharacterCounter=='on'):
        analyzed = ""
        counter = 0
        for char in djtext:
            counter+=1
        params = {'Purpose': 'ExtraSpaceRemover', 'analyzed_text': counter}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(removepunc!="on" and fullcaps!="on" and newlineRemover!="on" and ExtraSpaceRemover!="on" and CharacterCounter!="on"):
        return HttpResponse("Please Select Any Operation and Try again")
    return render(request, 'analyze.html', params)

def ex1(request):
    s = ''' <h1>Navigation Bar </h1><br>
    <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Vikrant </a><br>
    <a href="https://www.facebook.com/"> Facebook </a> <br>
    <a href="https://www.flipkart.com/"> Flipkart </a> <br>
    <a href="https://www.hindustantimes.com/"> News </a> <br>
    <a href="https://www.google.com/"> Google </a>'''
    return HttpResponse(s)
        






