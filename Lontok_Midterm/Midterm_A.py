from django.shortcuts import render
from django.http import HttpResponse

def jobroles(request):
    jobroles1 = 'reporting executive'
    jobroles2 = 'business analyst'
    jobroles3 = 'data analyst'

    return render (request, "midterma.html", {"jobroles1":jobroles1});
    