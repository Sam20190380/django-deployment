from django import template

register = template.Library()

@register.filter(name = 'cutting')
def cutting(value,arg):
    """
    CUTS OUT VALUES OF ARG FROM STRING

    """
    return value.replace(arg,'')
