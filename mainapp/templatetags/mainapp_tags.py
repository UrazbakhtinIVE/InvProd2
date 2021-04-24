import datetime

from django import template


register = template.Library()


@register.simple_tag
def test_days_to_diagnostics_remain(days, period):
    if days >= period:
        return "bg-success text-light"
    elif days >= period // 2:
        return "bg-warning text-dark"
    else:
        return "bg-danger text-light"




