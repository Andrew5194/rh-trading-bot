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

Create a `docker-compose.env` file and set the necessary environment variables needed for the RH Trading Bot:

> **Tip:** Use the provided `docker-compose.env.template` file and remove the `.template` suffix once env vars have been set.

```bash
POSTGRES_PASSWORD=""
POSTGRES_USER=""
POSTGRES_DB=""
RH_USERNAME=""
RH_PASSWORD=""
SLACK_BOT_TOKEN=""
SLACK_USER_ID=""
```

Then, spin up the RH Trading Bot services by their containers:

```bash
docker compose --env-file docker-compose.env up
```

You should see something similar to:

```bash
...
rh-trading-bot-postgres-1  | 2023-09-16 07:28:29.362 UTC [1] LOG:  database system is ready to accept connections
rh-trading-bot-slackbot-1  | DEBUG:urllib3.connectionpool:https://api.robinhood.com:443 "POST /oauth2/token/ HTTP/1.1" 200 None
rh-trading-bot-slackbot-1  | Input mfa code:
```

To input the MFA code, run the following in a separate terminal:

```bash
docker attach rh-trading-bot-slackbot-1
```

Then key in the MFA code in the separate terminal window. See [docker attach](https://docs.docker.com/engine/reference/commandline/attach/) for more details.

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