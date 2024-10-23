from django.shortcuts import render
from django.http import request, HttpResponse


def m_topic(request):
    return render(request, "m_topic.html")


def topic_disc(request):
    return render(request, "topic_disc.html")


def topic_disc_by_int(request, int_disc):
    return HttpResponse(f"ID DISCRIPTION: {int_disc}")
    # return render(request, "topic_disc_conv.html", context=id_disc) ---> Позже доделаю...

def topic_disc_by_slug(request, slug_disc):
    return HttpResponse(f"CAUGHT DISCRIPTION: {slug_disc}")

def topic_archi_year(request, arch_year):
    return HttpResponse(f"CAUGHT YEAR: {arch_year}")

