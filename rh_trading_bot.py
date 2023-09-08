"""A Robinhood Trading bot written in Python."""
import os
from pyrh import Robinhood

rh = Robinhood(username=os.getenv("RH_USERNAME"), password=os.getenv("RH_PASSWORD"))
rh.login()
