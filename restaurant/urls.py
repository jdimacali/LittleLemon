from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"booking", views.BookingViewSet)

urlpatterns = [
    path("api-token-auth/", obtain_auth_token),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("menu/", views.MenuItemsView.as_view(), name='menu'),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view(), name='menu-detail'),
    path("", include(router.urls)),
]
