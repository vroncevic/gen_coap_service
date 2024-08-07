# -*- coding: UTF-8 -*-

'''
Module
    read_template_test.py
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
    Defines class ReadTemplateTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ReadTemplate.
Execute
    python3 -m unittest -v read_template_test
'''

import sys
from typing import List
from os.path import dirname, realpath
from unittest import TestCase, main

try:
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from gen_coap_service.pro.read_template import ReadTemplate
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


class ReadTemplateTestCase(TestCase):
    '''
        Defines class ReadTemplateTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ReadTemplate.
        ReadTemplate unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_read_template_create - Test read templates create.
                | test_read_template_empty - Test read templates empty.
                | test_read_template_none - Test read templates None.
                | test_read_template - Test read templates.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_read_template_create(self) -> None:
        '''Test read templates create'''
        template_read = ReadTemplate()
        self.assertIsNotNone(template_read)

    def test_read_template_empty(self) -> None:
        '''Test read templates empty'''
        template_read = ReadTemplate()
        template_file: str = ''
        with self.assertRaises(ATSValueError):
            self.assertFalse(
                template_read.read(template_file)
            )

    def test_read_template_none(self) -> None:
        '''Test read templates None'''
        template_read = ReadTemplate()
        with self.assertRaises(ATSTypeError):
            self.assertFalse(
                template_read.read(None)  # type: ignore
            )

    def test_read_template(self) -> None:
        '''Test read templates'''
        template_read = ReadTemplate()
        current_dir: str = dirname(realpath(__file__))
        template_dir: str = f'{current_dir}/../gen_coap_service/conf/template/'
        template_files: List[str] = [
            f'{template_dir}coapthon/basic_resources.template',
            f'{template_dir}coapthon/coap_client.template',
            f'{template_dir}coapthon/coap_server.template',
            f'{template_dir}coapthon/logging.template'
        ]
        for template in template_files:
            self.assertTrue(bool(template_read.read(template)))


if __name__ == '__main__':
    main()
