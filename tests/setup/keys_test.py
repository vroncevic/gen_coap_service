# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenCoAPServiceBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_coap_service.setup.keys import GenCoAPServiceBundleKeys


class TestGenCoAPServiceBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenCoAPServiceBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenCoAPServiceBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenCoAPServiceBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenCoAPServiceBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenCoAPServiceBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenCoAPServiceBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenCoAPServiceBundleKeys.OPTION_INFO_FILE, opts)
