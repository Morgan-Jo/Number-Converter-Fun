from dataclasses import dataclass
from typing import Tuple

from rate_providers import StaticRateProvider, ExchangeRateProvider


@dataclass
class ConversionResult:
    amount: float
    from_currency: str
    to_currency: str
    rate: float
    converted_amount: float


class CurrencyConverter:
    def __init__(self, rate_provider: ExchangeRateProvider):
        self.rate_provider = rate_provider

    def convert(self, amount: float, from_currency: str, to_currency: str) -> ConversionResult:
        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        rate = self.rate_provider.get_rate(from_currency, to_currency)
        converted = round(amount * rate, 4)
        return ConversionResult(
            amount=amount,
            from_currency=from_currency.upper(),
            to_currency=to_currency.upper(),
            rate=rate,
            converted_amount=converted,
        )


def get_user_input() -> Tuple[float, str, str]:
    """
    Simple interactive function to read amount and currencies
    from the user.
    """
    while True:
        try:
            amount_str = input("Enter amount: ").strip()
            amount = float(amount_str)
            break
        except ValueError:
            print("Please enter a valid numeric amount.")

    from_currency = input("Enter from currency (e.g. GBP, EUR, USD): ").strip().upper()
    to_currency = input("Enter to currency (e.g. GBP, EUR, USD): ").strip().upper()

    return amount, from_currency, to_currency


def main():
    # Define static rates against a base currency (EUR here as example)
    static_rates = {
        "EUR": 1.0,
        "GBP": 0.86,
        "USD": 1.1,
        "JPY": 165.0,
        "AUD": 1.6,
    }

    provider = StaticRateProvider(base_currency="EUR", rates=static_rates)
    converter = CurrencyConverter(rate_provider=provider)

    print("Welcome to FlexRate: A Simple Currency Converter")
    print("Supported currencies:", ", ".join(sorted(static_rates.keys())))
    print()

    while True:
        try:
            amount, from_currency, to_currency = get_user_input()
            result = converter.convert(amount, from_currency, to_currency)
            print(
                f"Converted {result.amount:.2f} {result.from_currency} "
                f"to {result.converted_amount:.2f} {result.to_currency} "
                f"at rate {result.rate:.4f}"
            )
        except ValueError as e:
            print(f"Error: {e}")

        again = input("Do you want to convert another amount? [Y/n]: ").strip().lower()
        if again in {"n", "no"}:
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
