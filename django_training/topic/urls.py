from cgitb import handler
from django.urls import path, re_path
from . import views


urlpatterns = [

    path("disc/", views.topic_disc),                                          # http://127.0.0.1:8080/topic/disc/ - страница описания проекта
    path("disc/<int:int_disc>/", views.topic_disc_by_int),                    # http://127.0.0.1:8080/topic/disc/1..X/ - Балуемся с пользовательским конвертором (integer 0-XXXXX)
    path("disc/<slug:slug_disc>/", views.topic_disc_by_slug),                 # http://127.0.0.1:8080/topic/disc/бла-бла-бла/ - Балуемся с пользовательским конвертором (slug {text} without "/")
    re_path(r"^archive/(?P<arch_year>[0-9]{4})/",views.topic_archi_year),     # http://127.0.0.1:8080/topic/archive/1941/ - Балуемся с пользовательским конвертором
    # (Кастомная переменная arch_year, символы 0..9, 4 числа, примеры:{1234,9876,1941})

]





