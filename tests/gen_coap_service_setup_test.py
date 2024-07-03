# -*- coding: UTF-8 -*-

'''
Module
    gen_coap_service_setup_test.py
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
    Defines class GenCoAPTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of GenCoAP.
Execute
    python3 -m unittest -v gen_coap_service_setup_test
'''

import sys
from typing import List
from os.path import exists
from os import remove
from unittest import TestCase, main

try:
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from gen_coap_service.pro import GenCoAP
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_coap_service'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_coap_service/blob/dev/LICENSE'
__version__ = '1.1.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenCoAPTestCase(TestCase):
    '''
        Defines class GenCoAPTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of GenCoAP.
        GenCoAP unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create is not None.
                | test_get_reader - Is reader ok.
                | test_get_writer - Is writer ok.
                | test_gen_project_empty - Create project with missing name.
                | test_gen_project_none - Create project with None name.
                | test_gen_project_type_empty - Test missing type.
                | test_gen_project_type_none - Create project with None type.
                | test_gen_project_type_no_support - Test no support type.
                | test_gen_project - Create project.
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

    def test_default_create(self) -> None:
        '''Default on create is not None'''
        generator: GenCoAP = GenCoAP()
        self.assertIsNotNone(generator)

    def test_get_reader(self) -> None:
        '''Is reader ok'''
        generator: GenCoAP = GenCoAP()
        self.assertIsNotNone(generator.get_reader())

    def test_get_writer(self) -> None:
        '''Is writer ok'''
        generator: GenCoAP = GenCoAP()
        self.assertIsNotNone(generator.get_writer())

    def test_gen_project_empty(self) -> None:
        '''Create project with missing name'''
        generator: GenCoAP = GenCoAP()
        with self.assertRaises(ATSValueError):
            generator.project_setup('', 'coapthon')

    def test_gen_project_none(self) -> None:
        '''Create project with None name'''
        generator: GenCoAP = GenCoAP()
        with self.assertRaises(ATSTypeError):
            generator.project_setup(None, 'coapthon')

    def test_gen_project_type_empty(self) -> None:
        '''Test missing type'''
        generator: GenCoAP = GenCoAP()
        with self.assertRaises(ATSValueError):
            generator.project_setup('simple_project', '')

    def test_gen_project_type_none(self) -> None:
        '''Create project with None type'''
        generator: GenCoAP = GenCoAP()
        with self.assertRaises(ATSTypeError):
            generator.project_setup('simple_project', None)

    def test_gen_project_type_no_support(self) -> None:
        '''Test no support type'''
        generator: GenCoAP = GenCoAP()
        with self.assertRaises(ATSValueError):
            generator.project_setup('simple_project', 'some_type')

    def test_gen_project(self) -> None:
        '''Create project'''
        generator: GenCoAP = GenCoAP()
        self.assertTrue(generator.project_setup('simple_project', 'coapthon'))


if __name__ == '__main__':
    main()
