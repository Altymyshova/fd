from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def text1(reguest):
    culter = '''А культуре, особенно — христианская религия.'''
    return HttpResponse(culter)

def text2 (reguest):
    poznovatelno = '''какой то текст'''
    return HttpResponse(poznovatelno)

def text3 (reguest):
    urok1django = '''тоже текст'''
    return HttpResponse(urok1django)