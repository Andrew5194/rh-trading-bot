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


def bot_login(rh_object: Robinhood):
    """Authenticate RH Trading Bot with Robinhood."""
    rh_object.login()

    if rh_object.authenticated:
        logging.info("Successfully logged into Robinhood!")
    else:
        logging.info("Unable to authenticate with Robinhood.")
    return rh_object


def bot_slack_message(rh_object: Robinhood):
    """Use authenticated Robinhood to perform action and send notifications via Slackbot."""
    if rh_object is not Robinhood:
        logging.info(
            "Missing Robinhood object. Did you make sure to log in successfully?"
        )
        return
    client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
    try:
        response = client.chat_postMessage(
            channel=os.getenv("SLACK_USER_ID"),
            text=f"Your portfolio cash balance is {rh_object.get_account()['portfolio_cash']}",
        )
        logging.info(response)
    except SlackApiError as slack_api_error:
        print(f"Got an error: {slack_api_error.response['error']}")


rh_user = Robinhood(
    username=os.getenv("RH_USERNAME"), password=os.getenv("RH_PASSWORD")
)

auth_rh_user = bot_login(rh_user)
bot_slack_message(auth_rh_user)
