from django.urls import path

from generator.views import GeneratorView

urlpatterns = [
    path('', GeneratorView.as_view()),
    path('<int:number>',  GeneratorView.as_view()),
    path('flush', GeneratorView.as_view()),
    path('flush/<slug:table>', GeneratorView.as_view()),
]