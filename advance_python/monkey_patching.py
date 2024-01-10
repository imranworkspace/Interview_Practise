class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def patch_amount(self, new_amount):
        self.amount = new_amount


# Example usage
if __name__ == "__main__":
    # Create a Money object
    initial_money = Money(100, "USD")

    # Display initial money
    print("Initial Money:", initial_money)

    # Patch or update the amount
    new_amount = 150
    initial_money.patch_amount(new_amount)

    # Display patched money
    print("Patched Money:", initial_money)
