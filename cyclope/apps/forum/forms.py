#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright 2010-2013 Código Sur Sociedad Civil.
# All rights reserved.
#
# This file is part of Cyclope.
#
# Cyclope is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Cyclope is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
apps.forum.forms
-----
"""

from django import forms
from django.utils.translation import ugettext_lazy as _

from captcha.fields import CaptchaField

from models import Topic


class CreateTopicForm(forms.ModelForm):
    name = forms.CharField(label = _('Subject'), required=True)

    class Meta:
        model = Topic
        fields = ('name', 'text')

class CreateTopicCaptchaForm(forms.ModelForm):
    name = forms.CharField(label = _('Subject'), required=True)
    anonymous_name = forms.CharField(label = _('Your name'), required=True)
    captcha = CaptchaField(label=_("Security code"))

    class Meta:
        model = Topic
        fields = ('name', 'anonymous_name', 'text', )
