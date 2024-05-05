from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Mnoży value przez arg."""
    return value * arg