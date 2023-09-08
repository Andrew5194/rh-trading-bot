from pyrh import Robinhood
import os

rh = Robinhood(username=os.getenv("RH_USERNAME"), password=os.getenv("RH_PASSWORD"))
rh.login()