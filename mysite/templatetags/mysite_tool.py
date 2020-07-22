from django import template

register = template.Library()

@register.filter(name="getIdx")
def getIdx(list, arg):
    return list.index(arg)