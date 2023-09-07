# Robinhood Trading Bot

A robinhood trading bot. The trading bot uses the [Unofficial Robinhood API](https://github.com/robinhood-unofficial/pyrh) to communicate with Robinhood.

## Installation

To build the robinhood trading bot packaged within a Docker container, execute the following command from the root of this repo:

```bash
docker build -f Dockerfile .
```

Then, run the robinhood trading bot:

```bash
docker run -it <container> -e RH_USERNAME -e RH_PASSWORD 
```

docker run --env-file ./env.list ubuntu bash