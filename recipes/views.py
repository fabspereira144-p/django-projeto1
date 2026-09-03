from django.http import HttpResponse
from django.shortcuts import render


def home(response):
    return HttpResponse('HOME')

def contato(response):
    return HttpResponse('CONTATO')

def sobre(response):
    return HttpResponse('SOBRE')