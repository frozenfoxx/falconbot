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

## Environment Variables

## Command Line Arguments
