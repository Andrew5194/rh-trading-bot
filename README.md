# Robinhood Trading Bot

A Robinhood trading bot. The trading bot uses the [Unofficial Robinhood API](https://github.com/robinhood-unofficial/pyrh) to communicate with Robinhood and a [Slack Bot](https://api.slack.com/start/quickstart) to send notifications to a user.

![Build](https://github.com/Andrew5194/rh-trading-bot/actions/workflows/build.yml/badge.svg)
![Pylint](https://github.com/Andrew5194/rh-trading-bot/actions/workflows/pylint.yml/badge.svg)

## Installation

Let's get started! The fastest way to get up and running is through the [Quickstart](#quickstart) section. For developers wanting to experiment, look toward the [Building from Source](#building-from-source) section.

### Prerequisites

For obvious reasons, you will need to have an already established Robinhood account. In addition, to get notifications from the RH Trading bot, you will need to create your own Slack workspace and associated Slack Bot. Check out the following resources for tips on getting your Slack Workspace and Slack Bot up and running:

* [Creating a Slack Workspace](https://slack.com/help/articles/206845317-Create-a-Slack-workspace)
* [Creating a SlackBot](https://api.slack.com/start/quickstart)
* [Finding a Slack User ID](https://www.workast.com/help/article/how-to-find-a-slack-user-id/)

> **Note:** You will need to add the `chat:write` scope to your Slack Bot in order for it to send messages to your specified Slack user.

If your Slack Bot is properly set up, you should see something like the following when you run the RH Trading Bot:

![working-slackbot](.images/working-slackbot.png)

### Quickstart

First set the required environment variables by executing the following:

```bash
export RH_USERNAME=<your-robinhood-username>
export RH_PASSWORD=<your-robinhood-password>
export SLACK_BOT_TOKEN=<your-slack-bot-token>
export SLACK_USER_ID=<your-slack-user-id>
```

Then, pull the `rh-trading-bot` Docker image from Docker Hub and run the container while passing in the environment variables:

```bash
docker pull andrew5194/rh-trading-bot:main
docker run -it \
    -e RH_USERNAME \
    -e RH_PASSWORD \
    -e SLACK_BOT_TOKEN \
    -e SLACK_USER_ID \
    andrew5194/rh-trading-bot:main
```

### Building from Source

If you would like to experiment and build from source, execute the following command from the root of this repo to build a new local Docker container named `rh-trading-bot`:

```bash
docker build -f Dockerfile -t rh-trading-bot .
```

Then, run the locally built `rh-trading-bot` Docker container:

```bash
docker run -it \
    -e RH_USERNAME \
    -e RH_PASSWORD \
    -e SLACK_BOT_TOKEN \
    -e SLACK_USER_ID \
    rh-trading-bot
```

If you need to bypass the entrypoint script to access the container itself, run the following command:

```bash
docker run --entrypoint='' -it \
    -e RH_USERNAME \
    -e RH_PASSWORD \
    -e SLACK_BOT_TOKEN \
    -e SLACK_USER_ID \
    rh-trading-bot \
    bash
```

## Roadmap

The milestones upon the horizon.

### Features

- [X] Notifications
- [ ] Scheduler / Daily Reports
- [ ] Trade Analytics
- [ ] Algo Trading

### Deployment

- [ ] Docker Compose
- [ ] Terraform
- [ ] GKE