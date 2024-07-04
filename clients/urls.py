from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientCreateView, ClientListView, ClientDetailView, ClientUpdateView, ClientDeleteView

app_name = ClientsConfig.name

urlpatterns = [
    path("create/", ClientCreateView.as_view(), name="create client"),
    path("list/", ClientListView.as_view(), name="list client"),
    path("list/<int:pk>/", ClientDetailView.as_view(), name="detail client"),
    path("list/<int:pk>/", ClientUpdateView.as_view(), name="update client"),
    path("list/<int:pk>/", ClientDeleteView.as_view(), name="delete client"),
]