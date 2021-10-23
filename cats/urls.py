from django.urls import path
from cats import views

app_name = 'cats'
urlpatterns = [
    # path('', views.MainView.as_view(), name='all'),
    # path('cat/create/', views.CatCreate.as_view(), name='cat_create'),
    # path('cat/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    # path('cat/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
    # path('lookup/', views.BreedView.as_view(), name='breed_list'),
    # path('lookup/create/', views.BreedCreate.as_view(), name='breed_create'),
    # path('lookup/<int:pk>/update/',
    #      views.BreedUpdate.as_view(), name='breed_update'),
    # path('lookup/<int:pk>/delete/',
    #      views.BreedDelete.as_view(), name='breed_delete'),

    path('', views.BreedView.as_view(), name='breed_list'),
    path('cat/create/', views.BreedCreate.as_view(), name='breed_create'),
    path('cat/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    path('cat/<int:pk>/delete/',
         views.BreedDelete.as_view(), name='breed_delete'),

    path('lookup/', views.MainView.as_view(), name='all'),
    path('lookup/create/', views.CatCreate.as_view(), name='cat_create'),
    path('lookup/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('lookup/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
]
