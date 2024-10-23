from django.shortcuts import render
from django.http import request,HttpResponse

def m_topic(request):
    return render(request,"m_topic.html")

def topic_disc(request):
    return render(request, "topic_disc.html")


