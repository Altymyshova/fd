from django.http import HttpResponse
from django.shortcuts import render

# Create your views here


#dz1
from dzz.models import Comment


def text1(request):
    culter = '''А культуре, особенно — христианская религия.'''
    return HttpResponse(culter)

def text2 (request):
    poznovatelno = '''какой то текст'''
    return HttpResponse(poznovatelno)

def text3 (request):
    urok1django = '''тоже текст'''
    return HttpResponse(urok1django)



#dz2
def commentshow (request):
    comments = Comment.objects.all()
    context = {"comments": comments}
    return render(request,"shablon.html", context )


