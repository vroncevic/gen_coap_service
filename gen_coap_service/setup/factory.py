# -*- coding: UTF-8 -*-

'''
Module
    factory.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Factory for creating the gen_coap_service bundle.
'''

from __future__ import annotations

from os.path import abspath, dirname, join

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory

from gen_coap_service.setup.bundle import GenCoAPServiceBundle
from gen_coap_service.setup.options import GenCoAPServiceBundleOptions
from gen_coap_service.setup.registry import GenCoAPServiceBundleRegistry
from gen_coap_service.setup.dependencies import GenCoAPServiceBundleDependencies
from gen_coap_service.setup.opt_validator import GenCoAPServiceBundleOptionsValidator
from gen_coap_service.setup.keys import GenCoAPServiceBundleKeys
from gen_coap_service.core.service.engine import Service
from gen_coap_service.infrastructure.subprocessor import SubProcessor
from gen_coap_service.infrastructure.cli.engine import CLI
from gen_coap_service.infrastructure.cli.setup.bundle import CLIBundle
from gen_coap_service.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_coap_service.infrastructure.cli.setup.registry import CLIBundleRegistry
from gen_coap_service.infrastructure.command.command import CommandBundle
from gen_coap_service.infrastructure.command.gen_coap_service_command_definition import GenCoAPServiceCommandDefinition
from gen_coap_service.infrastructure.command.gen_coap_service_command_executor import GenCoAPServiceCommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_coap_service'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_coap_service/blob/dev/LICENSE'
__version__ = '1.1.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenCoAPServiceBundleFactory:
    '''
        Factory for creating the gen_coap_service bundle.

        It defines:

            :attributes:
                | _info_file - Path to the gen_coap_service info file.
            :methods:
                | create_bundle - Creates the gen_coap_service bundle with optional pre-configured options.
                | get_version - Returns the factory version.
    '''

    _info_file: str = join(
        dirname(dirname(abspath(__file__))), 'infrastructure', 'config', 'gen_coap_service.cfg'
    )

    @classmethod
    def create_bundle(cls, options: GenCoAPServiceBundleOptions | None = None) -> GenCoAPServiceBundle:
        '''
            Creates the gen_coap_service bundle with optional pre-configured options.

            :param options: The pre-configured options for the gen_coap_service bundle.
            :return: The gen_coap_service bundle.
            :exceptions:
                | ATSValueError: The gen_coap_service bundle options must be provided and have proper values.
                | ATSTypeError:  The gen_coap_service bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_coap_service bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_coap_service bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_coap_service bundle must be provided and have proper values.
                | ATSTypeError:  The gen_coap_service bundle must be an instance of GenCoAPServiceBundle and
                |                its attributes must be instances of their respective types.
        '''
        if options is not None:
            GenCoAPServiceBundleOptionsValidator.validate(options)

        info_file = options.get(GenCoAPServiceBundleKeys.OPTION_INFO_FILE) if options else cls._info_file

        context_bundle: ContextBundle = ContextBundleFactory.create_bundle()

        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        subprocessor: SubProcessor = SubProcessor(generator=base_bundle.generation_manager)

        service: Service = Service(subprocessor=subprocessor)

        gen_coap_service_definition: GenCoAPServiceCommandDefinition = GenCoAPServiceCommandDefinition()

        gen_coap_service_bundle: CommandBundle = CommandBundle(
            definition=gen_coap_service_definition,
            executor=GenCoAPServiceCommandExecutor(gen_coap_service_definition)
        )

        cli_bundle: CLIBundle = CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=service,
                parser=base_bundle.option_manager,
                commands=[gen_coap_service_bundle]
            )
        )

        cli: CLI = CLI(cli_bundle)

        return GenCoAPServiceBundleRegistry.create_bundle(
            dependencies=GenCoAPServiceBundleDependencies(
                base=base_bundle,
                service=service,
                subprocessor=subprocessor,
                cli=cli
            )
        )

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the factory version.

            :return: The factory version.
            :exceptions: None.
        '''
        return __version__
