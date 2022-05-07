# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
 Copyright
     Copyright (C) 2020 Vladimir Roncevic <elektron.ronca@gmail.com>
     gen_coap_service is free software: you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     gen_coap_service is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Defined class GenCoAPServiceSetup with attribute(s) and method(s).
     Generate module file generator_test.py by template and parameters.
'''

import sys
from os.path import dirname, realpath

try:
    from gen_coap_service.pro.read_template import ReadTemplate
    from gen_coap_service.pro.write_template import WriteTemplate
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, https://vroncevic.github.io/gen_coap_service'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_coap_service/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenCoAPServiceSetup(FileChecking):
    '''
        Defined class GenCoAPServiceSetup with attribute(s) and method(s).
        Generate module file generator_test.py by template and parameters.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | PRO_STRUCTURE - project setup (template, module).
                | __reader - reader API.
                | __writer - writer API.
                | __config - project setup in yaml format.
            :methods:
                | __init__ - initial constructor.
                | get_reader - getter for template reader.
                | get_writer - getter for template writer.
                | gen_setup - generate module file setup.py.
                | __str__ - dunder method for GenCoAPServiceSetup.
    '''

    GEN_VERBOSE = 'GEN_COAP_SERVICE::PRO::GEN_SETUP'
    PRO_STRUCTURE = '/../conf/project.yaml'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(GenCoAPServiceSetup.GEN_VERBOSE, verbose, 'init setup')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)
        project = '{0}/{1}'.format(
            dirname(realpath(__file__)), GenCoAPServiceSetup.PRO_STRUCTURE
        )
        self.check_path(file_path=project, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=project, file_format='yaml', verbose=verbose
        )
        if self.is_file_ok():
            yml2obj = Yaml2Object(project)
            self.__config = yml2obj.read_configuration()
        else:
            self.__config = None

    def get_reader(self):
        '''
            Getter for template reader.

            :return: template reader object.
            :rtype: <ReadTemplate>
            :exceptions: None
        '''
        return self.__reader

    def get_writer(self):
        '''
            Getter for template writer.

            :return: template writer object.
            :rtype: <WriteTemplate>
            :exceptions: None
        '''
        return self.__writer

    def select_pro_type(self, verbose=False):
        '''
            Select form type.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: project template selected | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        template_selected = None
        if bool(self.__config):
            types = self.__config['templates']
            type_names = self.__config['types']
            pro_types_len = len(types)
            for index, pro_type in enumerate(type_names):
                print(
                    '{0} {1}'.format(index + 1, pro_type)
                )
                verbose_message(
                    GenCoAPServiceSetup.GEN_VERBOSE, verbose,
                    'to be processed template', pro_type
                )
            while True:
                input_type = input(' select project type: ')
                options = range(1, pro_types_len + 1, 1)
                try:
                    if int(input_type) in list(options):
                        template_selected = types[int(input_type) - 1]
                        break
                    else:
                        raise ValueError
                except ValueError:
                    error_message(
                        GenCoAPServiceSetup.GEN_VERBOSE,
                        'not an appropriate choice'
                    )
            verbose_message(
                GenCoAPServiceSetup.GEN_VERBOSE, verbose,
                'selected', template_selected
            )
        return template_selected

    def gen_setup(self, pro_name, verbose=False):
        '''
            Generate module generator_test.py.

            :param pro_name: project name.
            :type pro_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('str:pro_name', pro_name)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        status, setup_content = False, None
        verbose_message(
            GenCoAPServiceSetup.GEN_VERBOSE, verbose,
            'generating project', pro_name
        )
        selected_project_type = self.select_pro_type(verbose=verbose)
        if bool(selected_project_type):
            setup_content = self.__reader.read(
                selected_project_type, verbose=verbose
            )
            if setup_content:
                status = self.__writer.write(
                    setup_content, pro_name, verbose=verbose
                )
        return status

    def __str__(self):
        '''
            Dunder method for GenCoAPServiceSetup.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            str(self.__reader), str(self.__writer)
        )
