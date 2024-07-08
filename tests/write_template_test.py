# -*- coding: UTF-8 -*-

'''
Module
    write_template_test.py
Copyright
    Copyright (C) 2020 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_coap_service is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_coap_service is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class WriteTemplateTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of WriteTemplate.
Execute
    python3 -m unittest -v write_template_test
'''

import sys
from os.path import exists, dirname, realpath
from os import remove
from typing import Any, List, Dict
from unittest import TestCase, main

try:
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from gen_coap_service.pro.read_template import ReadTemplate
    from gen_coap_service.pro.write_template import WriteTemplate
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_coap_service'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_coap_service/blob/dev/LICENSE'
__version__ = '1.1.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplateTestCase(TestCase):
    '''
        Defines class WriteTemplateTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of WriteTemplate.
        WriteTemplate unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_write_template_create - Test write templates create.
                | test_write_template_empty - Test write templates empty.
                | test_write_template_none - Test write templates None.
                | test_write_template - Test write templates.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''
        if exists('basic_resources.py'):
            remove('basic_resources.py')
        if exists('coap_client.py'):
            remove('coap_client.py')
        if exists('coap_server.py'):
            remove('coap_server.py')
        if exists('logging.conf'):
            remove('logging.conf')

    def test_write_template_create(self) -> None:
        '''Test write templates create'''
        template_write = WriteTemplate()
        self.assertIsNotNone(template_write)

    def test_write_template_empty(self) -> None:
        '''Test write templates empty'''
        template_write = WriteTemplate()
        content: Dict[Any, Any] = {}
        with self.assertRaises(ATSValueError):
            self.assertFalse(
                template_write.write(content)
            )

    def test_write_template_none(self) -> None:
        '''Test write templates None'''
        template_write = WriteTemplate()
        with self.assertRaises(ATSTypeError):
            self.assertFalse(
                template_write.write(None)  # type: ignore
            )

    def test_write_template(self) -> None:
        '''Test write templates'''
        template_read = ReadTemplate()
        template_write = WriteTemplate()
        pro_data: Dict[Any, Any] = {}
        pro_data['name'] = 'simple_test'
        pro_data['type'] = 'coapthon'
        current_dir: str = dirname(realpath(__file__))
        template_dir: str = f'{current_dir}/../gen_coap_service/conf/template/'
        template_files: List[str] = [
            f'{template_dir}coapthon/basic_resources.template',
            f'{template_dir}coapthon/coap_client.template',
            f'{template_dir}coapthon/coap_server.template',
            f'{template_dir}coapthon/logging.template'
        ]
        modules: List[str] = [
            'basic_resources.py',
            'coap_client.py',
            'coap_server.py',
            'logging.conf'
        ]
        for template, module in zip(template_files, modules):
            pro_data['template'] = template_read.read(template)
            pro_data['module'] = module
            self.assertTrue(
                template_write.write(pro_data)
            )


if __name__ == '__main__':
    main()
