# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2018 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################
import os
from django.apps import AppConfig as BaseAppConfig


def run_setup_hooks(*args, **kwargs):
    from django.conf import settings
    from .celeryapp import app as celeryapp

    LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))
    project_templates = os.path.join(LOCAL_ROOT, "templates")
    settings.TEMPLATES[0]["DIRS"] = [project_templates] + [d for d in settings.TEMPLATES[0]["DIRS"] if d != project_templates]

    if celeryapp not in settings.INSTALLED_APPS:
        settings.INSTALLED_APPS += (celeryapp,)


class AppConfig(BaseAppConfig):
    name = "geonode_project"
    label = "geonode_project"

    def ready(self):
        super(AppConfig, self).ready()
        run_setup_hooks()
