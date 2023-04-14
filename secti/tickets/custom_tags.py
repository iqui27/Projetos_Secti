from django import template

register = template.Library()

@register.simple_tag
def days_difference(date1, date2):
    difference = date2 - date1
    return difference.days
