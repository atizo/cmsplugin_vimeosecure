# -*- coding: utf-8 -*-
#
# Atizo - The Open Innovation Platform
# http://www.atizo.com/
#
# Copyright (c) 2008-2010 Atizo AG. All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#

from django import template
from django.utils.safestring import mark_safe
from django.conf import settings
from django.utils.encoding import force_unicode, smart_str

register = template.Library()

def vs_textilerestricted(value):
    
    try:
        import textile
        from textile.functions import textile_restricted
    except ImportError:
        if settings.DEBUG:
            raise template.TemplateSyntaxError("Error in {% textile %} filter: The Python textile library isn't installed.")
        return force_unicode(value)
    else:
        return mark_safe(force_unicode(textile_restricted(smart_str(value), lite=False)))
        textile.is_safe = True    

vs_textilerestricted.is_safe = True
register.filter(vs_textilerestricted)
