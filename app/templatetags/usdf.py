from django import template
register=template.Library()
def swap(value):
    return value.swapcase()  
@register.filter()
def count(value):
    return value.count()

@register.filter(name='rem')
def remove(value,arg):
    return value.replace(arg,'')

register.filter('swapping',swap) 
register.filter('counting',count)
register.filter('removing',remove)   