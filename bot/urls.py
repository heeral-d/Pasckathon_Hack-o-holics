from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('getsql/', views.get_sql, name='getsql'),
    path('record/', views.record, name='record'),
    path('trans/', views.trans, name='trans')
]