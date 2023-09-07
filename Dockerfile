FROM python:slim-bookworm

COPY . /
RUN python --version && pip install -r requirements.txt

RUN ["chmod", "+x", "./entrypoint.sh"]
ENTRYPOINT [ "./entrypoint.sh" ]
