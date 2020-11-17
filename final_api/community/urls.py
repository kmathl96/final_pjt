from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path('<int:review_pk>/update/', views.update, name='update'),
    path('<int:review_pk>/delete/', views.delete, name='delete'),
    path('<int:review_pk>/create_comment/', views.create_comment, name="create_comment"),
    path('<int:review_pk>/<int:comment_pk>/update/', views.update_comment, name="update_comment"),
    path('<int:review_pk>/<int:comment_pk>/delete/', views.delete_comment, name="delete_comment"),
    path('<int:review_pk>/comment_list/', views.comment_list, name="comment_list"),
]