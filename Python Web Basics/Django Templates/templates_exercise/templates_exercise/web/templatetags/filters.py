from django.template import Library

register = Library()


@register.filter('odd')
def get_odd_values(values):
    return [x for x in values if x % 2 == 1]


@register.filter('date_style')
def format_date_style(date):
    return date.strftime('%y/%m/%d')