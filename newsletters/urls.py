from django.urls import path
from newsletters.apps import NewslettersConfig
from newsletters.views import (
    NewsletterCreateView,
    NewsletterListView,
    NewsletterDetailView,
    NewsletterUpdateView,
    NewsletterDeleteView,
)

app_name = NewslettersConfig.name

urlpatterns = [
    path("create/", NewsletterCreateView.as_view(), name="create newsletter"),
    path("list/", NewsletterListView.as_view(), name="list newsletter"),
    path("list/<int:pk>/", NewsletterDetailView.as_view(), name="detail newsletter"),
    path("list/<int:pk>/", NewsletterUpdateView.as_view(), name="update newsletter"),
    path("list/<int:pk>/", NewsletterDeleteView.as_view(), name="delete newsletter"),
]
