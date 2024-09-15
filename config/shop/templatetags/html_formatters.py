from django import template

def productimage(value):
    return f"{value}"

register = template.Library()

register.simple_tag(productimage)

