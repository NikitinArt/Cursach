from django.urls import path
from .views import index, create, delete, update
from .views import InvestView

urlpatterns = [
    path('', index, name='home'),
    path('create', create, name='create'),
    path('delete', delete, name='delete'),
    path('update', update, name='update'),
    path('api', InvestView.as_view(), name='api'),
]