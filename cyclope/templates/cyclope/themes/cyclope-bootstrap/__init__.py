# *-- coding:utf-8 --*
"""Configuration for the Neutrona theme templates and regions.

Attributes:
    verbose_name: name of theme to be displayed in the admin interface
    layout_templates: dictionary defining regions for the available templates
"""

from django.utils.translation import ugettext_lazy as _

verbose_name = _('Cyclope-Bootstrap')

layout_templates = {

    'default.html':
        {
        'verbose_name': _('Default'),
        'regions' : {
            'header': _('Header'),
            'left': _('Left'),
            'right': _('Right'),
            'top': _('Top'),
            'bottom': _('Bottom'),
            'footer': _('Footer'),
            }
        },

    'main.html':
        {
        'verbose_name': _('Main'),
        'regions' : {
            'header': _('Header'),
            'left': _('Left'),
            'right': _('Right'),
            'top': _('Top'),
            'bottom': _('Bottom'),
            'footer': _('Footer'),
            }
        },
    'empty.html':
        {'verbose_name': _('Empty'),
         'regions': {}
         },

    'newsletter.html':
        {'verbose_name': _('Newsletter'),
        'regions' : {
            'header': _('header'),
            'before_content': _('before content'),
            'after_content': _('after content'),
            }
         },
}


region_ids = {
    'content': '',
    'left': '',
    'right': 'sidebar',
    'top': '',
    'bottom': '',
}

region_classes = {
    'content': '',
    'left': '',
    'bottom': '',
    'right': 'col-xs-6 col-sm-3 sidebar-offcanvas',
}

content_classes = {
    'content': '',
    'left': '',
    'bottom': 'col-xs-12 col-sm-12 col-md-6 col-lg-4',
    'right': '',
}
