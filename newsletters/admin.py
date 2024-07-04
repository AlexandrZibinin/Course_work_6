from django.contrib import admin

from newsletters.models import Newsletter


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        "first_send",
        "period",
        "status",
    )
