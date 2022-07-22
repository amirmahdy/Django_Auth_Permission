from django.urls import path, include
from .views import LoginView, TestView


urlpatterns = [
    path('login/',LoginView.as_view(), name="login"),
    path('captcha/', include('rest_captcha.urls'), name='captcha'),

    path('test/',TestView.as_view(), name="test"),
]