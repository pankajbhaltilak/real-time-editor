from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('editor/<int:doc_id>/', views.document_editor, name='document_editor'),
    path('grammar-check/', views.grammar_suggestions, name='grammar_check'),
    path('create/', views.create_document, name='create_document')

]