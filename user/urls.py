from django.urls import path
from .views import signin, signup, signout

app_name = 'user'

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("signin/", signin, name='signin'),
    path("signout/", signout, name="signout"),
]
