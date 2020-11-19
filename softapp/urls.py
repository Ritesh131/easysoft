# Apps Url

from django.urls import path
from .views import index, QuerySubmit

urlpatterns = [
    path('', index.as_view()),
    path('submitsuccess', QuerySubmit)
]
