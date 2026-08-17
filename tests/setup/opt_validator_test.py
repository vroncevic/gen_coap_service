# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for GenCoAPServiceBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from gen_coap_service.setup.opt_validator import GenCoAPServiceBundleOptionsValidator


class TestGenCoAPServiceBundleOptionsValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        GenCoAPServiceBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            GenCoAPServiceBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenCoAPServiceBundleOptionsValidator.validate("not_a_mapping")

    def test_validate_invalid_option_type(self) -> None:
        with self.assertRaises(Exception):
            options = {'info_file': 123}
            GenCoAPServiceBundleOptionsValidator.validate(options)

    def test_is_valid_success(self) -> None:
        options = {'info_file': 'some_path'}
        self.assertTrue(GenCoAPServiceBundleOptionsValidator.is_valid(options))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenCoAPServiceBundleOptionsValidator.is_valid(None))
        self.assertFalse(GenCoAPServiceBundleOptionsValidator.is_valid("not_a_mapping"))
        self.assertFalse(GenCoAPServiceBundleOptionsValidator.is_valid({'info_file': 123}))
