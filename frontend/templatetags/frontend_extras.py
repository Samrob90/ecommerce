from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
@stringfilter
def convert_string_to_array(value, arg):
    list = value.split(" ")
    return list[arg]
