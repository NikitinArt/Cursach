from django.urls import path
from .views import InvestView

urlpatterns = [
    path('', InvestView.as_view(), name='api'),
    path('<int:pk>', InvestView.as_view())
]
