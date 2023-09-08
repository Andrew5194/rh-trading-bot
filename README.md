# Robinhood Trading Bot

A Robinhood trading bot. The trading bot uses the [Unofficial Robinhood API](https://github.com/robinhood-unofficial/pyrh) to communicate with Robinhood.

![Docker Build](https://github.com/Andrew5194/rh-trading-bot/actions/workflows/docker-build-push.yml/badge.svg)
![Pylint](https://github.com/Andrew5194/rh-trading-bot/actions/workflows/pylint.yml/badge.svg)

## Roadmap

- [ ] Notifications
- [ ] Trade Analytics
- [ ] Algo Trading

## Installation

Let's get started! The fastest way to get up and running is through the [Quickstart](#quickstart) section. For developers wanting to experiment, look toward the [Building from Source](#building-from-source) section.

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

If you would like to experiment and build from source, execute the following command from the root of this repo to build a new local Docker container named `rh-trading-bot`:

```bash
docker build -f Dockerfile -t rh-trading-bot .
```

Then, run the locally built `rh-trading-bot` Docker container:

```bash
docker run -it -e RH_USERNAME \
    -e RH_PASSWORD \
    rh-trading-bot
```
