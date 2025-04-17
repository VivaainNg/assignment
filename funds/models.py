from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _


class Fund(models.Model):
    """
    Data model for Fund class
    - Fund ID
    - Fund Name
    - Fund Manager Name
    - Fund Description
    - Fund Net Asset Value (NAV)
    - Fund Date of Creation
    - Fund Performance (as a percentage)

    """

    name = models.CharField(verbose_name=_("Fund Name"), max_length=128, unique=True)
    manager_name = models.CharField(verbose_name=_("Fund Manager Name"), max_length=128)
    description = models.TextField(verbose_name=_("Fund Description"), max_length=512)
    net_asset_value = models.DecimalField(
        verbose_name=_("Fund Net Asset Value"),
        max_digits=14,
        decimal_places=2,
        default=Decimal("0"),
        help_text=_("NAV"),
    )
    date_creation = models.DateField(verbose_name=_("Fund Date of Creation"))
    performance = models.DecimalField(
        verbose_name=_("Fund Performance"),
        max_digits=8,
        decimal_places=2,
        help_text=_("As a percentage"),
    )

    def __str__(self) -> str:
        return f"{self.name}"
