from django.urls import path

from . import views

urlpatterns = [
    # path("january", views.january),
    # path("february", views.february),
    # path("march", views.march),
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challange_by_number),
    path("<str:month>", views.monthly_challange, name="monthly-challange"),
]