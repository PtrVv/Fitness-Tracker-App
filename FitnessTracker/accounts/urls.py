from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.urls.conf import include

from FitnessTracker.accounts.views import UserRegistrationView, ProfileDetailsView, EditProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileDetailsView.as_view(), name='profile-details'),
    path('<int:pk>/', include([
        path('profile-edit/', EditProfileView.as_view(), name='profile-edit'),
    ]))
]
