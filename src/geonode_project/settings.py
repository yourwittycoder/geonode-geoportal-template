# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
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

# Django settings for the GeoNode project.
import os

# Load more settings from a file called local_settings.py if it exists
try:
    from geonode_project.local_settings import *
#    from geonode.local_settings import *
except ImportError:
    from geonode.settings import *

# Register the Sustain GeoPortal project app
INSTALLED_APPS = tuple(INSTALLED_APPS) + (
    "geonode_project.apps.AppConfig",
)

# Sustain GeoPortal: use direct OGR/PostGIS import instead of dynamic models
IMPORTER_ENABLE_DYN_MODELS = False

# Sustain GeoPortal custom middleware
MIDDLEWARE = MIDDLEWARE + (
)

#
# General Django development settings
#
PROJECT_NAME = "sustain_geoportal"

# add trailing slash to site url. geoserver url will be relative to this
if not SITEURL.endswith("/"):
    SITEURL = "{}/".format(SITEURL)

SITENAME = os.getenv("SITENAME", "sustain_geoportal")

# Defines the directory that contains the settings file as the LOCAL_ROOT
# It is used for relative settings elsewhere.
LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

WSGI_APPLICATION = "geonode_project.wsgi.application"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = os.getenv("LANGUAGE_CODE", "en")


# Location of url mappings
ROOT_URLCONF = "geonode_project.urls"

# Additional directories which hold static files
# - Give priority to local geonode-project ones
STATICFILES_DIRS = [
    os.path.join(LOCAL_ROOT, "static"),
] + STATICFILES_DIRS

# Location of locale files
LOCALE_PATHS = (os.path.join(LOCAL_ROOT, "locale"),) + LOCALE_PATHS

PROJECT_TEMPLATE_DIR = os.path.join(LOCAL_ROOT, "templates")

TEMPLATES[0]["DIRS"] = [
    PROJECT_TEMPLATE_DIR,
    *[d for d in TEMPLATES[0]["DIRS"] if d != PROJECT_TEMPLATE_DIR],
]
loaders = TEMPLATES[0]["OPTIONS"].get("loaders") or [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]
# loaders.insert(0, 'apptemplates.Loader')
TEMPLATES[0]["OPTIONS"]["loaders"] = loaders
TEMPLATES[0].pop("APP_DIRS", None)


PROJECT_FIXTURES = [
    # List project-related fixture files here, in the order they should be loaded.
]

# Disable Memcached cache for Sustain GeoPortal
if "memcached" in CACHES:
    del CACHES["memcached"]
