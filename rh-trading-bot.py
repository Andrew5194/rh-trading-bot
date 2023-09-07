import robin_stocks.robinhood as rh

login_response = rh.authentication.login(store_session=False)

account_profile_response = rh.profiles.load_account_profile()
print(f"Your current cash account balance is: {account_profile_response['cash_balances']['cash']}")

