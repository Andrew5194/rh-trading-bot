# Robinhood Trading Bot

A robinhood trading bot. The trading bot uses the [Unofficial Robinhood API](https://github.com/robinhood-unofficial/pyrh) to communicate with Robinhood.

## Installation

Pull the Robinhood trading bot Docker image from Docker Hub and run the container by executing the following:

```bash
docker run -it Andrew5194:rh-trading-bot:latest
```

If you want to build from source, execute the following command from the root of this repo:

```bash
docker build -f Dockerfile .
```

Then, run the locally built Robinhood trading bot:

```bash
docker run -it <container>
```