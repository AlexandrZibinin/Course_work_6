from django.urls import path

from letters.apps import LettersConfig
from letters.views import LetterCreateView, LetterListView, LetterDetailView, LetterUpdateView, LetterDeleteView

app_name = LettersConfig.name

urlpatterns = [
    path("create/", LetterCreateView.as_view(), name="create Letter"),
    path("list/", LetterListView.as_view(), name="list Letter"),
    path("list/<int:pk>/", LetterDetailView.as_view(), name="detail Letter"),
    path("list/<int:pk>/", LetterUpdateView.as_view(), name="update Letter"),
    path("list/<int:pk>/", LetterDeleteView.as_view(), name="delete Letter"),
]