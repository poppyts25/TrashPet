from django import template
register = template.Library()

#access dictionary using variable as key

@register.filter
def keyvalue(dict, key):    
    return dict[key]