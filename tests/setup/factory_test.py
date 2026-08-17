# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenCoAPServiceBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_coap_service.setup.bundle import GenCoAPServiceBundle
from gen_coap_service.setup.factory import GenCoAPServiceBundleFactory


class TestGenCoAPServiceBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenCoAPServiceBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenCoAPServiceBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_coap_service/infrastructure/config/gen_coap_service.cfg'}
        bundle = GenCoAPServiceBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenCoAPServiceBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenCoAPServiceBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenCoAPServiceBundleFactory.get_version(), '1.1.6')
