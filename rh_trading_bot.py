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
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

logging.basicConfig(level=logging.DEBUG)


def bot_login(rh_object: Robinhood):
    """Authenticate RH Trading Bot with Robinhood."""
    logging.info(
        "Attempting to authenticate RH Trading Bot, use the docker attach command to input the MFA for this container."
    )
    rh_object.login()

    if rh_object.authenticated:
        logging.info("RH Trading Bot is now authenticated with Robinhood.")
    else:
        logging.info("RH Trading Bot failed to authenticate with Robinhood.")
    return rh_object


def bot_slack_message(rh_object: Robinhood):
    """Use authenticated Robinhood to perform action and send notifications via Slackbot."""
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


def bot_extract_data():
    """Extract data and push to Postgres."""
    pg_user = os.getenv("POSTGRES_USER")
    pg_password = os.getenv("POSTGRES_PASSWORD")
    pg_database = os.getenv("POSTGRES_DB")

    # PostgreSQL database URL
    DATABASE_URL = (
        f"postgresql+psycopg2://{pg_user}:{pg_password}@postgres/{pg_database}"
    )

    # Create PostgreSQL database connection
    engine = create_engine(DATABASE_URL)

    # Connect to the database
    connection = engine.connect()

    # Create MetaData object
    metadata = MetaData()

    # Define 'users' table
    users = Table(
        "users",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("username", String),
        Column("email", String),
    )

    # Create the table in the database
    metadata.create_all(engine)

    # Execute a query to add a new user
    connection.execute(
        users.insert().values(username="john_doe", email="john@example.com")
    )

    # Execute a query to fetch all users
    result = connection.execute(users.select())

    # Print fetched users
    for row in result:
        print(row)

    # Close the connection
    connection.close()


auth_rh_user = bot_login(rh_user)
bot_slack_message(auth_rh_user)
bot_extract_data()
