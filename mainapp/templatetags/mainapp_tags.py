import math

from django import template


register = template.Library()


@register.simple_tag
def test_days_to_diagnostics_remain(days, period):
    if not days and not period:
        return ""

    if days <= 0:
        return "bg-danger text-light"

    K = math.floor((days / period) * 10)
    if K <= 2:
        return "bg-danger text-light"
    elif K <= 3:
        return "bg-warning text-dark"
    elif K <= 5 or K >= 5:
        return "bg-success text-light"




