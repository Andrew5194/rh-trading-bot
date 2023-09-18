FROM python:slim-bookworm

COPY entrypoint.sh rh_trading_bot.py requirements.txt /

RUN python --version && pip install -r requirements.txt

RUN ["chmod", "+x", "./entrypoint.sh"]
ENTRYPOINT [ "./entrypoint.sh" ]
