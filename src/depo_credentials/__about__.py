# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__","__requirements__"
]

__requirements__ = ["django_unmaskpasswordinput","django-fernet-fields","depo"]
__title__ = "depo_credentials"
__summary__ = "Credential management for Depo"
__uri__ = "https://git01.pfsfhq.com/Operations/NetDM/homepage/"

__version__ = "1.0.0a0"

__author__ = "Primerica Network Team"
__email__ = "networkteam@primerica.com"

__license__ = "BSD or Apache License, Version 2.0"
__copyright__ = "Copyright 2019 {}".format(__author__)
__includedata__ = True
__includedatafiles__ = {'' : ['','']}
__excludedatafiles__ = {}
