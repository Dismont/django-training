from django.contrib import admin
from django.urls import path, include,re_path
from topic import views


urlpatterns = [
    path('admin/', admin.site.urls),        # http://127.0.0.1:8080/admin/ - страница Администратора*

    # URLS FOR APPLICATION TOPIC

    path("topic/", views.m_topic),                                             # http://127.0.0.1:8080/topic/ - основная страница
    path("topic/disc/", views.topic_disc),                                     # http://127.0.0.1:8080/topic/disc/ - страница описания проекта
    path("topic/disc/<int:int_disc>/", views.topic_disc_by_int),               # http://127.0.0.1:8080/topic/disc/1..X/ - Балуемся с пользовательским конвертором (integer 0-XXXXX)
    path("topic/disc/<slug:slug_disc>/", views.topic_disc_by_slug),            # http://127.0.0.1:8080/topic/disc/бла-бла-бла/ - Балуемся с пользовательским конвертором (slug {text} without "/")
    re_path(r"^topic/archive/(?P<arch_year>[0-9]{4})/",views.topic_archi_year),     # http://127.0.0.1:8080/topic/archive/1941/ - Балуемся с пользовательским конвертором
    # (Кастомная переменная arch_year, символы 0..9, 4 числа, примеры:{1234,9876,1941})
]
