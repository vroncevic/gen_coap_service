# -*- coding: UTF-8 -*-

'''
Module
    validator_test.py
Info
    Unit tests for GenCoAPServiceBundleValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from ats_utilities.base.setup.bundle import BaseBundle

from gen_coap_service.core.service.iservice import IService
from gen_coap_service.core.service.isubprocessor import ISubProcessor
from gen_coap_service.infrastructure.cli.icli import ICLI
from gen_coap_service.setup.bundle import GenCoAPServiceBundle
from gen_coap_service.setup.validator import GenCoAPServiceBundleValidator


class DummyService:

    def execute(self, *, params: object) -> object:
        return None

    def is_initialized(self) -> bool:
        return True


class DummySubProcessor:

    def run(self, *, params: object) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class DummyCLI:

    def run(self) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class TestGenCoAPServiceBundleValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        bundle = GenCoAPServiceBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        GenCoAPServiceBundleValidator.validate(bundle)

    def test_validate_bundle_none(self) -> None:
        with self.assertRaises(Exception):
            GenCoAPServiceBundleValidator.validate(None)

    def test_validate_bundle_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenCoAPServiceBundleValidator.validate("invalid_bundle")

    def test_validate_missing_components(self) -> None:
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        with self.assertRaises(Exception):
            bundle = GenCoAPServiceBundle(
                base=None,
                service=dummy_service,
                subprocessor=dummy_subprocessor,
                cli=dummy_cli
            )
            GenCoAPServiceBundleValidator.validate(bundle)

    def test_validate_invalid_component_types(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        with self.assertRaises(Exception):
            bundle = GenCoAPServiceBundle(
                base="invalid",
                service=dummy_service,
                subprocessor=dummy_subprocessor,
                cli=dummy_cli
            )
            GenCoAPServiceBundleValidator.validate(bundle)

        with self.assertRaises(Exception):
            bundle = GenCoAPServiceBundle(
                base=mock_base,
                service="invalid",
                subprocessor=dummy_subprocessor,
                cli=dummy_cli
            )
            GenCoAPServiceBundleValidator.validate(bundle)

        with self.assertRaises(Exception):
            bundle = GenCoAPServiceBundle(
                base=mock_base,
                service=dummy_service,
                subprocessor="invalid",
                cli=dummy_cli
            )
            GenCoAPServiceBundleValidator.validate(bundle)

        with self.assertRaises(Exception):
            bundle = GenCoAPServiceBundle(
                base=mock_base,
                service=dummy_service,
                subprocessor=dummy_subprocessor,
                cli="invalid"
            )
            GenCoAPServiceBundleValidator.validate(bundle)

    def test_is_valid_success(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        bundle = GenCoAPServiceBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )
        self.assertTrue(GenCoAPServiceBundleValidator.is_valid(bundle))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenCoAPServiceBundleValidator.is_valid(None))
        self.assertFalse(GenCoAPServiceBundleValidator.is_valid("invalid"))
