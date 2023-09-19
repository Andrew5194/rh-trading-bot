#!/bin/bash

until pg_isready -h postgres -U postgres -p 5432 ; do sleep 5 ; done

echo "Starting robinhood trading bot..."
python /rh_trading_bot.py