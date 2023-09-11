# Copyright (c) 2023, Andrew5194 / Andrew Yang
# All rights reserved.

# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""A Robinhood Trading bot written in Python."""
import os
import logging
from pyrh import Robinhood
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logging.basicConfig(level=logging.DEBUG)

rh = Robinhood(username=os.getenv("RH_USERNAME"), password=os.getenv("RH_PASSWORD"))
rh.login()
account_profile = rh.get_account()

client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
try:
    response = client.chat_postMessage(
        channel=os.getenv("SLACK_USER_ID"),
        text=f"Your portfolio cash account balance is {account_profile['portfolio_cash']}",
    )
except SlackApiError as e:
    print(f"Got an error: {e.response['error']}")
