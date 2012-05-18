#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2010-2012 Código Sur - Nuestra América Asoc. Civil / Fundación Pacificar.
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

# based on  shestera's django-multisite
# http://github.com/shestera/django-multisite

from threading import local

_thread_locals = local()

class DynamicSetting(object):
    def __init__(self, setting_name, *args):
        # the name of the setting whose value we will hold in _thread_locals
        self.setting_name = setting_name
        if len(args) > 1:
            raise TypeError("DynamicSetting only supports one value")
        elif len(args) == 1:
            self.set(args[0])

    def set(self, value):
        "Sets the value for this setting in _thread_locals"
        if isinstance(value, tuple):
            tuple_format = "%s__tuple-%s"
            value = tuple([DynamicSetting(tuple_format % (self.setting_name, n), element)
                           for n, element in enumerate(value)])
        if isinstance(value, dict):
            dic = {}
            for key, val in value.iteritems():
                dict_format = "%s__dict-%s"
                dic[key] = DynamicSetting(dict_format % (self.setting_name, key), val)
            value = dic
        setattr(_thread_locals, self.setting_name, value)

    def get_value(self):
        "Gets the settings actual value"
        return getattr(_thread_locals, self.setting_name, None)

    def __getitem__(self, attr):
        return self.get_value().__getitem__(attr)

    def __setitem__(self, attr, value):
        raise NotImplemented

    def __getattribute__(self, attr):
        if attr == 'setting_name':
            return super(DynamicSetting, self).__getattribute__(attr)

        current = getattr(_thread_locals, self.setting_name, None)
        if hasattr(current, attr):
            return getattr(current, attr)
        else:
            return super(DynamicSetting, self).__getattribute__(attr)

    def __unicode__(self):
        return unicode(self.get_value())

    def __str__(self):
        return str(self.get_value())

    def __repr__(self):
        return "<DynamicSetting: %s>" % repr(self.get_value())

    def __float__(self):
        return float(self.get_value())

    def __nonzero__(self):
        return bool(self.get_value())



class RequestHostHook(object):
    def __repr__(self):
        if not hasattr(_thread_locals, "REQUEST_HOST"):
            _thread_locals.REQUEST_HOST = ""
        return _thread_locals.REQUEST_HOST

    def set(self, value):
        _thread_locals.REQUEST_HOST = value

    def get(self):
        return _thread_locals.REQUEST_HOST

    def get_module_name(self):
        return repr(self)


class MediaRootHook(object):
    def __repr__(self):
        if not hasattr(_thread_locals, "MEDIA_ROOT"):
            _thread_locals.MEDIA_ROOT = ""
        return _thread_locals.MEDIA_ROOT

    def set(self, value):
        _thread_locals.MEDIA_ROOT = value

    def endswith(self, val):
        return str(self).endswith(val)

    def __add__(self, other):
        return str(self) + other


