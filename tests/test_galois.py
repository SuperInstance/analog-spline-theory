"""Tests for Galois Unification Visualizer."""

import pytest
import importlib
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Module has hyphen in name, use importlib
mod = importlib.import_module("galois-unification-visualizer")
GaloisConnection = mod.GaloisConnection
PARTS = mod.PARTS
verify_unified_structure = mod.verify_unified_structure


class TestGaloisConnection:
    def test_creation(self):
        gc = GaloisConnection(
            name="test", domain_name="A", codomain_name="B",
            alpha_desc="fwd", beta_desc="bwd",
            unit_holds=True, counit_holds=True, de_morgan_holds=True,
        )
        assert gc.name == "test"
        assert gc.check() is True

    def test_check_fails_without_unit(self):
        gc = GaloisConnection(
            name="test", domain_name="A", codomain_name="B",
            alpha_desc="fwd", beta_desc="bwd",
            unit_holds=False, counit_holds=True, de_morgan_holds=True,
        )
        assert gc.check() is False

    def test_check_fails_without_counit(self):
        gc = GaloisConnection(
            name="test", domain_name="A", codomain_name="B",
            alpha_desc="fwd", beta_desc="bwd",
            unit_holds=True, counit_holds=False, de_morgan_holds=True,
        )
        assert gc.check() is False

    def test_unit_and_counit_sufficient(self):
        gc = GaloisConnection(
            name="test", domain_name="A", codomain_name="B",
            alpha_desc="fwd", beta_desc="bwd",
            unit_holds=True, counit_holds=True, de_morgan_holds=False,
        )
        assert gc.check() is True

class TestParts:
    def test_six_parts(self):
        assert len(PARTS) == 6

    def test_all_parts_check(self):
        for part in PARTS:
            assert part.check(), f"{part.name} failed check"

    def test_all_have_descriptions(self):
        for part in PARTS:
            assert len(part.alpha_desc) > 0
            assert len(part.beta_desc) > 0

    def test_boolean_and_heyting_mixed(self):
        boolean = [p for p in PARTS if p.de_morgan_holds]
        heyting = [p for p in PARTS if not p.de_morgan_holds]
        assert len(boolean) == 4
        assert len(heyting) == 2

class TestVerify:
    def test_verify_returns_true(self):
        assert verify_unified_structure() is True
