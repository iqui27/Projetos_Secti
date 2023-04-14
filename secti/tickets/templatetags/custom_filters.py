from django import template

register = template.Library()

@register.filter
def to_hours_minutes(value):
    if not value:
        return ''

    total_seconds = int(value.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60

    return f'{hours} horas {minutes} minutos'
