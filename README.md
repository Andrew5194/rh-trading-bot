# Robinhood Trading Bot

A Robinhood trading bot. The trading bot uses the [Unofficial Robinhood API](https://github.com/robinhood-unofficial/pyrh) to communicate with Robinhood.

![Docker Image CI](https://github.com/Andrew5194/rh-trading-bot/actions/workflows/docker-image.yml/badge.svg)

## Installation

Pull the Robinhood trading bot Docker image from Docker Hub and run the container by executing the following:

```bash
docker run -it Andrew5194:rh-trading-bot:main
```

If you would like to build from source, execute the following command from the root of this repo:

```bash
docker build -f Dockerfile .
```

Then, run the locally built Robinhood trading bot:

```bash
docker run -it <container>
```