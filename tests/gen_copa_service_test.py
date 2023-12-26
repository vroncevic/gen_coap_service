# -*- coding: UTF-8 -*-

'''
Module
    gen_coap_service_test.py
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
    Defines class GenCoAPServiceTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of GenCoAPService.
Execute
    python3 -m unittest -v gen_coap_service_test
'''

import sys
from typing import List
from os.path import exists
from os import remove
from unittest import TestCase, main

try:
    from gen_coap_service import GenCoAPService
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_coap_service'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_coap_service/blob/dev/LICENSE'
__version__ = '1.1.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenCoAPServiceTestCase(TestCase):
    '''
        Defines class GenCoAPServiceTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of GenCoAPService.
        GenCoAPService uni        if exists('basic_resources.py'):
            remove('basic_resources.py')
        if exists('coap_client.py'):
            remove('coap_client.py')
        if exists('coap_server.py'):
            remove('coap_server.py')
        if exists('logging.conf'):
            remove('logging.conf')t tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create (not None).
                | test_missing_args - Test missing args.
                | test_wrong_arg_name - Test wrong arg name.
                | test_wrong_arg_type - Test wrong arg type.
                | test_process - Generate project structure.
                | test_gen_coaplib - Generate libcoap structure.
                | test_gen_node_coap - Generate node_coap structure.
                | test_tool_not_operational - Test not operational.
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
        '''Default on create (not None)'''
        generator: GenCoAPService = GenCoAPService()
        self.assertIsNotNone(generator)

    def test_missing_args(self) -> None:
        '''Test missing args'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_coap_service_run.py')
        generator: GenCoAPService = GenCoAPService()
        self.assertFalse(generator.process())

    def test_wrong_arg_name(self) -> None:
        '''Test wrong arg name'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_coap_service_run.py')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'coapthon')
        sys.argv.insert(4, '-d')
        sys.argv.insert(5, 'simple_project')
        generator: GenCoAPService = GenCoAPService()
        self.assertFalse(generator.process())

    def test_wrong_arg_type(self) -> None:
        '''Test wrong arg type'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_coap_service_run.py')
        sys.argv.insert(2, '-d')
        sys.argv.insert(3, 'coapthon')
        sys.argv.insert(4, '-g')
        sys.argv.insert(5, 'simple_project')
        generator: GenCoAPService = GenCoAPService()
        self.assertFalse(generator.process())

    def test_process(self) -> None:
        '''Generate project structure'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_coap_service_run.py')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'coapthon')
        sys.argv.insert(4, '-g')
        sys.argv.insert(5, 'simple_project')
        generator: GenCoAPService = GenCoAPService()
        self.assertTrue(generator.process())

    def test_gen_coaplib(self) -> None:
        '''Generate libcoap structure'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_coap_service_run.py')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'libcoap')
        sys.argv.insert(4, '-g')
        sys.argv.insert(5, 'simple_project')
        generator: GenCoAPService = GenCoAPService()
        self.assertTrue(generator.process())

    def test_gen_node_coap(self) -> None:
        '''Generate node_coap structure'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_coap_service_run.py')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'node_coap')
        sys.argv.insert(4, '-g')
        sys.argv.insert(5, 'simple_project')
        generator: GenCoAPService = GenCoAPService()
        self.assertTrue(generator.process())

    def test_tool_not_operational(self) -> None:
        '''Test not operational'''
        sys.argv.clear()
        sys.argv.insert(0, 'python3')
        sys.argv.insert(1, 'gen_coap_service_run.py')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'coapthon')
        sys.argv.insert(4, '-g')
        sys.argv.insert(5, 'simple_project')
        generator: GenCoAPService = GenCoAPService()
        generator.tool_operational = False
        self.assertFalse(generator.process())


if __name__ == '__main__':
    main()
