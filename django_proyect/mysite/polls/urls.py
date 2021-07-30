from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

app_name = 'polls'

router = SimpleRouter()

router.register(r"questions_serialized", views.QuestionsView)

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
] + router.urls
