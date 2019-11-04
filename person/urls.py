from django.urls import path

from person.views import PersonView

urlpatterns = [
    path('', PersonView.as_view()),
    path('<int:number>', PersonView.as_view()),
]