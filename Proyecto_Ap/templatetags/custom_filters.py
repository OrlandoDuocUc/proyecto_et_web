from django import template

register = template.Library()

@register.filter
def currency_format(value):
    try:
        value = float(value)
    except (ValueError, TypeError):
        return value  #DEVUELVE EL VALOR ORIGINAL, SI ES QUE NO PUEDE CONVERTIRLO EN FLOAT
    return "${:,.0f}".format(value)

@register.filter
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return value
    
 
