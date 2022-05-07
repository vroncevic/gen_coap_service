#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
 Module
     setup.py
 Copyright
     Copyright (C) 2020 Vladimir Roncevic <elektron.ronca@gmail.com>
     gen_coap_service is free software: you can redistribute it and/or
     modify it under the terms of the GNU General Public License as published
     by the Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     gen_coap_service is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define setup for tool gen_coap_service.
'''

from __future__ import print_function
import sys
from os.path import abspath, dirname, join, exists
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, https://vroncevic.github.io/gen_coap_service'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_coap_service/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


def install_directory():
    '''
        Return the installation directory, or None.

        :return: path (success) | None.
        :rtype: <str> | <NoneType>
        :exceptions: None
    '''
    py_version = '{0}.{1}'.format(sys.version_info[0], sys.version_info[1])
    if '--github' in sys.argv:
        index = sys.argv.index('--github')
        sys.argv.pop(index)
        paths = (
            '{0}/lib/python{1}/dist-packages/'.format(sys.prefix, py_version),
            '{0}/lib/python{1}/site-packages/'.format(sys.prefix, py_version)
        )
    else:
        paths = (s for s in (
            '{0}/local/lib/python{1}/dist-packages/'.format(
                sys.prefix, py_version
            ),
            '{0}/local/lib/python{1}/site-packages/'.format(
                sys.prefix, py_version
            )
        ))
    message = None
    for path in paths:
        message = '[setup] check path {0}'.format(path)
        print(message)
        if exists(path):
            message = '[setup] use path {0}'.format(path)
            print(message)
            return path
    message = '[setup] no installation path found, check {0}\n'.format(
        sys.prefix
    )
    print(message)
    return None


INSTALL_DIR = install_directory()
TOOL_DIR = 'gen_coap_service/'
CONF, TEMPLATE, LOG = 'conf', 'conf/template', 'log'
COAPTHON = 'conf/template/coapthon'
COAP_CLIENT = 'conf/template/coap_client'
COAP_SERVER = 'conf/template/coap_server'
NODE = 'conf/template/node_coap'
if not bool(INSTALL_DIR):
    print('[setup] force exit from install process')
    sys.exit(127)
THIS_DIR, LONG_DESCRIPTION = abspath(dirname(__file__)), None
with open(join(THIS_DIR, 'README.md')) as readme:
    LONG_DESCRIPTION = readme.read()
PROGRAMMING_LANG = 'Programming Language :: Python ::'
VERSIONS = [
    '2.7', '3', '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9'
]
SUPPORTED_PY_VERSIONS = [
    '{0} {1}'.format(PROGRAMMING_LANG, VERSION) for VERSION in VERSIONS
]
LICENSE_PREFIX = 'License :: OSI Approved ::'
LICENSES = [
    'GNU Lesser General Public License v2 (LGPLv2)',
    'GNU Lesser General Public License v2 or later (LGPLv2+)',
    'GNU Lesser General Public License v3 (LGPLv3)',
    'GNU Lesser General Public License v3 or later (LGPLv3+)',
    'GNU Library or Lesser General Public License (LGPL)'
]
APPROVED_LICENSES = [
    '{0} {1}'.format(LICENSE_PREFIX, LICENSE) for LICENSE in LICENSES
]
PYP_CLASSIFIERS = SUPPORTED_PY_VERSIONS + APPROVED_LICENSES
setup(
    name='gen_coap_service',
    version='1.0.0',
    description='Generating CoAP Modules',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_coap_service',
    license='GPL 2020 Free software to use and distributed it.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='Unix, Linux, Development, CoAP, Modules',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=['gen_coap_service', 'gen_coap_service.pro'],
    install_requires=['ats-utilities'],
    package_data={
        'gen_coap_service': [
            '{0}/{1}'.format(CONF, 'gen_coap_service.logo'),
            '{0}/{1}'.format(CONF, 'gen_coap_service.cfg'),
            '{0}/{1}'.format(CONF, 'gen_coap_service_util.cfg'),
            '{0}/{1}'.format(CONF, 'project.yaml'),
            '{0}/{1}'.format(COAPTHON, 'basic_resources.template'),
            '{0}/{1}'.format(COAPTHON, 'coap_client.template'),
            '{0}/{1}'.format(COAPTHON, 'coap_server.template'),
            '{0}/{1}'.format(COAPTHON, 'logging.template'),
            '{0}/{1}'.format(COAP_CLIENT, 'AUTHORS.template'),
            '{0}/{1}'.format(COAP_CLIENT, 'autogen.template'),
            '{0}/{1}'.format(COAP_CLIENT, 'ChangeLog.template'),
            '{0}/{1}'.format(COAP_CLIENT, 'configure.template'),
            '{0}/{1}'.format(COAP_CLIENT, 'INSTALL.template'),
            '{0}/{1}'.format(COAP_CLIENT, 'Makefile.template'),
            '{0}/{1}'.format(COAP_CLIENT, 'NEWS.template'),
            '{0}/{1}'.format(COAP_CLIENT, 'README.template'),
            '{0}/{1}'.format(COAP_CLIENT, 'src/client_api.template'),
            '{0}/{1}'.format(COAP_CLIENT, 'src/main.template'),
            '{0}/{1}'.format(COAP_CLIENT, 'src/Makefile.template'),
            '{0}/{1}'.format(COAP_CLIENT, 'src/print_error.template'),
            '{0}/{1}'.format(COAP_CLIENT, 'src/print_success.template'),
            '{0}/{1}'.format(COAP_CLIENT, 'src/print_usage.template'),
            '{0}/{1}'.format(COAP_CLIENT, 'src/print_verbose.template'),
            '{0}/{1}'.format(COAP_CLIENT, 'src/process_options.template'),
            '{0}/{1}'.format(COAP_CLIENT, 'src/time_handler.template'),
            '{0}/{1}'.format(COAP_SERVER, 'AUTHORS.template'),
            '{0}/{1}'.format(COAP_SERVER, 'autogen.template'),
            '{0}/{1}'.format(COAP_SERVER, 'ChangeLog.template'),
            '{0}/{1}'.format(COAP_SERVER, 'configure.template'),
            '{0}/{1}'.format(COAP_SERVER, 'INSTALL.template'),
            '{0}/{1}'.format(COAP_SERVER, 'Makefile.template'),
            '{0}/{1}'.format(COAP_SERVER, 'NEWS.template'),
            '{0}/{1}'.format(COAP_SERVER, 'README.template'),
            '{0}/{1}'.format(COAP_SERVER, 'src/get_date.template'),
            '{0}/{1}'.format(COAP_SERVER, 'src/get_full.template'),
            '{0}/{1}'.format(COAP_SERVER, 'src/get_time.template'),
            '{0}/{1}'.format(COAP_SERVER, 'src/main.template'),
            '{0}/{1}'.format(COAP_SERVER, 'src/Makefile.template'),
            '{0}/{1}'.format(COAP_SERVER, 'src/server_api.template'),
            '{0}/{1}'.format(COAP_SERVER, 'src/time_handler.template'),
            '{0}/{1}'.format(NODE, 'client.template'),
            '{0}/{1}'.format(NODE, 'server.template'),
            '{0}/{1}'.format(TEMPLATE, 'rpi_pico_coap/TODO'),
            '{0}/{1}'.format(TEMPLATE, 'template_coapthon.yaml'),
            '{0}/{1}'.format(TEMPLATE, 'template_COAP_SERVER.yaml'),
            '{0}/{1}'.format(TEMPLATE, 'template_node_coap.yaml'),
            '{0}/{1}'.format(TEMPLATE, 'template_rpi_pico_coap.yaml'),
            '{0}/{1}'.format(LOG, 'gen_coap_service.log')
        ]
    },
    data_files=[(
        '/usr/local/bin/', [
            '{0}{1}'.format(TOOL_DIR, 'run/gen_coap_service_run.py')
        ]
    )]
)
