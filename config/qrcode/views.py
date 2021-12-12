from django.shortcuts import render

'''
qrcode views
'''
from django.shortcuts import render, redirect

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Model


# Create your views here.

def qrcode_view(request):
    template = 'qrcode/qrcode.html'

    context = {}

    return render(request, template, context)
