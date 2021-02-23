
from django.contrib import admin
from django.urls import path, include

from subscription.views import UserSubscriptionView, RemoveSubscriptionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subscription/', UserSubscriptionView.as_view()),
    path('remove-subscription/<int:id>/', RemoveSubscriptionView.as_view()),
]
