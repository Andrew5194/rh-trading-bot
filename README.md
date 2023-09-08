# Robinhood Trading Bot

A Robinhood trading bot. The trading bot uses the [Unofficial Robinhood API](https://github.com/robinhood-unofficial/pyrh) to communicate with Robinhood.

![Docker Image CI](https://github.com/Andrew5194/rh-trading-bot/actions/workflows/docker-image.yml/badge.svg)

## Roadmap

- [ ] Notifications
- [ ] Trade Analytics
- [ ] Algo Trading

## Installation

### Quickstart

First set the required `RH_USERNAME` and `RH_PASSWORD` environment variables by executing the following:

```bash
export RH_USERNAME=<your-robinhood-username>
export RH_PASSWORD=<your-robinhood-password>
```

Then, pull the `rh-trading-bot` Docker image from Docker Hub and run the container while passing in the environment variables:

```bash
docker run -it -e RH_USERNAME \
    -e RH_PASSWORD \
    andrew5194/rh-trading-bot:main
```

### Building from Source

If you would like to build from source, execute the following command from the root of this repo:

```bash
docker build -f Dockerfile .
```

Then, run the locally built Robinhood trading bot:

```bash
docker run -it <container>
```
