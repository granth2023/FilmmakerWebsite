"""
URL configuration for mybackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp.views import home, search_movie, MovieViewSet, MovieCollectionViewSet, EventViewSet, DiscussionBoardViewSet, CommentViewSet, LikeCreateDestroyView, RSVPViewSet 
from rest_framework.routers import DefaultRouter 
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'collections', MovieCollectionViewSet)
router.register(r'events', EventViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeCreateDestroyView, basename='like')
router.register(r'rsvps', RSVPViewSet)
router.register(r'discussionboards', DiscussionBoardViewSet)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('search-movie/<title>/', search_movie, name='search-movie'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('api/', include(router.urls)),
   ]