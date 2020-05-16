from django import template

register = template.Library()


@register.filter
def divide(value, arg):
    try:
        if value % arg == 1:
            return int(value) // int(arg) + 1
        else:
            return None
    except (ValueError, ZeroDivisionError):
        return None


@register.filter
def in_between(value, limit):
    try:
        if 4 < value <= limit + 4:
            print(value)
            return True
        else:
            return False
    except:
        return False
