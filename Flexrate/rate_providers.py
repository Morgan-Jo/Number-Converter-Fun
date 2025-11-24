from abc import ABC, abstractmethod
from typing import Dict


class ExchangeRateProvider(ABC):
    """Abstract base class for exchange rate providers."""

    @abstractmethod
    def get_rate(self, from_currency: str, to_currency: str) -> float:
        """Return the rate to convert 1 unit of from_currency into to_currency."""
        raise NotImplementedError


class StaticRateProvider(ExchangeRateProvider):
    """
    Simple static provider using a base currency and a dictionary of rates
    relative to that base. For example, base EUR and rates like:
    {"EUR": 1.0, "GBP": 0.86, "USD": 1.1}
    """

    def __init__(self, base_currency: str, rates: Dict[str, float]):
        self.base_currency = base_currency.upper()
        self.rates = {code.upper(): rate for code, rate in rates.items()}

        if self.base_currency not in self.rates:
            raise ValueError("Base currency must be included in rates dictionary.")

    def get_rate(self, from_currency: str, to_currency: str) -> float:
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.rates:
            raise ValueError(f"Unsupported from_currency: {from_currency}")

        if to_currency not in self.rates:
            raise ValueError(f"Unsupported to_currency: {to_currency}")

        # Convert via base currency
        rate_from = self.rates[from_currency]
        rate_to = self.rates[to_currency]

        # Rate to go from from_currency to base, then base to to_currency
        # base_amount = amount / rate_from
        # target_amount = base_amount * rate_to
        # So rate = rate_to / rate_from
        return rate_to / rate_from


# Optional: placeholder for a live API provider
# You can fill this in once you choose an API.
class ApiRateProvider(ExchangeRateProvider):
    """
    Example skeleton for live API based rates. You would need to:
    - Pick a real API
    - Add your API key if needed
    - Handle network errors
    """

    def __init__(self, api_url: str):
        self.api_url = api_url

    def get_rate(self, from_currency: str, to_currency: str) -> float:
        raise NotImplementedError(
            "ApiRateProvider is not implemented yet. Use StaticRateProvider for now."
        )