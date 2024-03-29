from django import template

register = template.Library()


@register.filter()
def formatize(val):
    try:
        if val is not None:
            val = float(val)
            return f'{val:,.2f}'

        return val
    except Exception:
        return val
    
@register.filter()
def slash(string):
    result=""
    for char in string:
        result+=char+'/'
    return result



@register.filter()
def show_title(val1, val2):
    return val1[:int(val2)]

@register.filter()
def get_description_length(description):
    length = len(description)

    if length % 2 == 0:
        return description[:50]
    elif length % 3 == 0:
        return description[:51]
    else:
        return description[:49]