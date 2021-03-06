# -*- coding: utf-8 -*-
from django.contrib.admin.views.main import SEARCH_VAR
from django.template import Library

register = Library()


@register.inclusion_tag('admin/templatetags/tabs.html')
def views_tabs(views, name=None, obj=None):
    """
    Render extra views as tabs.
    """
    return {'views': views, 'name': name, 'object': obj}


@register.inclusion_tag('admin/search_form.html')
def contextual_search_form(search_url, search_fields):
    return {
        'search_url': search_url,
        'search_fields': search_fields,
        'search_var': SEARCH_VAR,
    }
