from django import template

register=template.Library()


def swap(value):
    return value.swapcase()

@register.filter()
def remove(value,args):
    return value.replace(args,"")

@register.filter(name='counting')
def counting(value,args):
    c=0
    for i in range(len(value)):
        if value[i:i+len(args):]==args:
            c+=1
    return c

register.filter('swapping',swap)
