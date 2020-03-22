import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel

from hub.models import NGO


class PaymentOrder(TimeStampedModel):
    ngo = models.ForeignKey(NGO, related_name="payment_orders", null=True, blank=True, on_delete=models.SET_NULL)

    order_id = models.CharField(
        _("Order ID"), max_length=100, blank=True, unique=True, default=uuid.uuid4, editable=False
    )

    first_name = models.CharField(_("First name"), max_length=254)
    last_name = models.CharField(_("Last name"), max_length=254)
    phone = models.CharField(_("Phone"), max_length=30)
    email = models.EmailField(_("Email"),)
    address = models.CharField(_("Address"), max_length=254)
    details = models.TextField(_("Details"))
    amount = models.FloatField(_("Amount"))
    date = models.DateTimeField(_("Registered on"), auto_now_add=True)

    def __str__(self):
        return f"[{self.ngo.name}] {self.first_name} {self.last_name} {self.amount}"

    class Meta:
        verbose_name_plural = _("Payment Orders")
        verbose_name = _("Payment Order")


class PaymentResponse(TimeStampedModel):
    payment_order = models.ForeignKey(
        PaymentOrder, null=True, blank=True, related_name="responses", on_delete=models.SET_NULL
    )
    action = models.CharField(max_length=100, null=True, blank=True)
    error_code = models.CharField(max_length=100, null=True, blank=True)
    error_type = models.CharField(max_length=100, null=True, blank=True)
    error_message = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(_("Registered on"), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Payment Orders")
        verbose_name = _("Payment Order")
