from cgitb import handler
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),            # http://127.0.0.1:8080/admin/ - страница Администратора*
    # URLS FOR APPLICATION TOPIC
    path("topic/", include("topic.urls")),      # http://127.0.0.1:8080/topic/ - основная страница

]
handler404 = 'topic.views.page_not_found'
