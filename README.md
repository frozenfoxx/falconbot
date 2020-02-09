# falconbot

An automated bot that watches social media accounts.

Docker Hub: [https://hub.docker.com/r/frozenfoxx/falconbot/](https://hub.docker.com/r/frozenfoxx/falconbot/)

# How to Build

## Docker

To build the container for falconbot use the standard Docker build workflow:

```
clone git@github.com:frozenfoxx/falconbot.git
cd falconbot
docker build -t frozenfoxx/falconbot:latest .
```

# Usage

## Quickstart

## Docker

To use the Docker container in CLI mode simply run without options:

```
docker run -it \
  --rm \
  --name=falconbot \
  frozenfoxx/falconbot:latest
```

# Configuration

## Configuration File

The configuration file is located in `/etc/falconbot/conf/falconbot.conf`. It contains all primary and default options. An example file is as follows:

```
[DEFAULT]
acct_password = awesomepassword
acct_username = frozenfoxx
service = twitter
token = BIGSCARYTOKEN
```

## Environment Variables

Configuration file variables can be overridden by using the environment variables. All environment variables are the same as the command line argument, only in uppercase.

* `ACCT_PASSWORD`: account password.
* `ACCT_USERNAME`: account username.
* `CONFIG`: path to the config file.
* `ENVIRONMENT`: config environment (default: `DEFAULT`).
* `SERVICE`: target service.
* `TOKEN`: API token.

## Command Line Arguments

Configuration can also be supplied via the CLI as arguments. These have precedence over environment variables and configuration file variables.
* `acct_password`: account password.
* `acct_username`: account username.
* `config`: path to the config file.
* `environment`: config environment (default: `DEFAULT`).
* `service`: target service.
* `token`: API token.
