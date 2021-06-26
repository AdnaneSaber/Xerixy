
from django import template

register = template.Library()


@register.simple_tag
def media(value):
    return f'/media/{value}'
