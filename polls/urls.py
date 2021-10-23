from django.urls import path
from .views import IndexView, owner, DetailView, ResultsView, vote


app_name = 'polls'

urlpatterns = [
    # added by IOAN
    path('', IndexView.as_view(), name='index'),
    path('owner', owner, name='owner'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
]
