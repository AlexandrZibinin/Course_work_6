from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from newsletters.models import Newsletter


class NewsletterCreateView(CreateView):
    model = Newsletter
    fields = "__all__"
    success_url = reverse_lazy("newsletters:list")


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterDetailView(DetailView):
    model = Newsletter


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    fields = "__all__"
    success_url = reverse_lazy("newsletters:list")


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy("newsletters:list")
