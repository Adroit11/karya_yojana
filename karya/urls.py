from django.urls import path
from .views import IndexView, CreateAccountView
from django.views.generic.base import TemplateView


app_name = 'karya'

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('register/', CreateAccountView.as_view(template_name = 'karya/register.html'), name='register_url')
]
