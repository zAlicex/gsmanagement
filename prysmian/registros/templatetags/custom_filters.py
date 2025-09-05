from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def format_currency(value):
    try:
        return f"R$ {float(value):,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
    except (ValueError, TypeError):
        return "R$ 0,00"

@register.filter
def format_currency_mx(value):
    """
    Format currency for Mexico using Mexican Peso symbol (MX$)
    """
    try:
        return f"MX$ {float(value):,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
    except (ValueError, TypeError):
        return "MX$ 0,00"

@register.filter
def format_currency_cr(value):
    """
    Format currency for Costa Rica using Costa Rican Colón symbol (₡)
    """
    try:
        return f"₡ {float(value):,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
    except (ValueError, TypeError):
        return "₡ 0,00"
