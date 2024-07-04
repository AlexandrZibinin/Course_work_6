from django.db import models


class Newsletter(models.Model):
    first_send = models.DateTimeField(
        auto_now=False, auto_now_add=False, verbose_name="дата и время первой отправки"
    )
    period = models.PositiveSmallIntegerField(
        blank=True, null=True, verbose_name="период отправки"
    )
    status = models.BooleanField(verbose_name="статус отправки")
    client = models.ManyToManyField("clients.Client", verbose_name="получатель")
    message = models.ForeignKey(
        "letters.Letter",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="сообщение",
    )

    def __str__(self):
        return f"{self.first_send}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
