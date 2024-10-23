from django.contrib import admin
from django.urls import path, include
from topic import views


urlpatterns = [
    path('admin/', admin.site.urls),        # http://127.0.0.1:8080/admin/

    # URLS FOR APPLICATION TOPIC

    path("topic/", views.m_topic),          # http://127.0.0.1:8080/topic/
    path("topic/disc/",views.topic_disc)
]
