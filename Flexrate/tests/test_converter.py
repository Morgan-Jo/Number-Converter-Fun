import pytest

from currency_converter import CurrencyConverter
from rate_providers import StaticRateProvider


def test_simple_conversion():
    rates = {"EUR": 1.0, "GBP": 0.8}
    provider = StaticRateProvider(base_currency="EUR", rates=rates)
    converter = CurrencyConverter(provider)

    result = converter.convert(100, "EUR", "GBP")
    assert pytest.approx(result.converted_amount, 0.0001) == 80.0


def test_inverse_conversion():
    rates = {"EUR": 1.0, "GBP": 0.8}
    provider = StaticRateProvider(base_currency="EUR", rates=rates)
    converter = CurrencyConverter(provider)

    result = converter.convert(80, "GBP", "EUR")
    assert pytest.approx(result.converted_amount, 0.0001) == 100.0


def test_invalid_currency():
    rates = {"EUR": 1.0}
    provider = StaticRateProvider(base_currency="EUR", rates=rates)
    converter = CurrencyConverter(provider)

    with pytest.raises(ValueError):
        converter.convert(10, "EUR", "USD")


def test_negative_amount():
    rates = {"EUR": 1.0, "GBP": 0.8}
    provider = StaticRateProvider(base_currency="EUR", rates=rates)
    converter = CurrencyConverter(provider)

    with pytest.raises(ValueError):
        converter.convert(-5, "EUR", "GBP")
