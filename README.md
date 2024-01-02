
---

# REDASH NLP CHATBOT ANALYTICS

## Introduction

The Redash ChatGPT Plugin is an integration that brings natural language conversation capabilities powered by ChatGPT to your Redash dashboard. With this plugin, Redash users can engage in interactive and conversational queries, as well as visualize data directly from the chat interface.

## Features

- Conversational Queries: Users can interact with Redash using natural language queries, making the process more intuitive and user-friendly.
- Interactive Responses: ChatGPT generates human-like responses, providing users with informative and contextual feedback on their queries.
- Data Visualization: The plugin allows users to visualize query results directly within the chat interface, enabling faster data exploration and analysis.

The Redash ChatGPT Plugin is an exciting project that aims to integrate natural language conversation capabilities powered by ChatGPT into your Redash dashboard. Although the plugin is still a work in progress, it currently provides functionality for engaging in conversational queries with ChatGPT directly within the Redash interface.

## Requirements Before Installation

### Local development setup

#### Set up the prerequisites

Install needed packages:

```bash
$ sudo apt -y install docker.io docker-buildx docker-compose-v2
$ sudo apt -y install build-essential curl docker-compose pwgen python3-venv xvfb
```

#### Add your user to the "docker" group

```bash
$ sudo usermod -aG docker $USER
```

#### Install Node Version Manager

```bash
$ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
```

Now log out of your desktop, then back in again, for the group change to become effective and nvm to be available.

#### Install NodeJS version 16

Yes, it's End Of Life. But we need to use version 16 for now until we've updated some other stuff.

```bash
$ nvm install --lts 16
$ nvm alias default 16
$ nvm use 16
```

Confirm version 16 of NodeJS is active:

```bash
$ nvm list
```

#### Install Yarn 1.x

```bash
$ npm install --global yarn@1.22.19
```

#### Clone the Redash source code and install the NodeJS dependencies

```bash
$ git clone https://github.com/birehan/Redash-NLP-Chatbot-Analytics
$ cd redash
$ yarn
```

#### Generate your local environment variables file

Generate the .env file containing (required) environment variables, suitable for development builds:

```bash
$ make env
```
- _Final step_ Inside your `.env` file, add your OpenAI API key, with the name indicated below:

**Get your free OpenAI key** - https://platform.openai.com/

```bash
OPENAI_API_KEY=*****************************************
```
#### Compile and build

Redash uses GNU Make to run things, so if you're not sure about something it's often a good idea to take a look over the Makefile which can help.

#### Build the Redash front end

```bash
$ make build
```

#### Build local Redash Docker image

```bash
$ make compose_build
```

On my desktop (Ryzen 5600X) that took about 12 minutes to complete the first time. After that though, it's much faster at about a minute and a half each time.

It's a good idea to check that the docker images were built ok. We do that by telling docker to show us the local "docker images", which should include these three new ones. It's important the "created" time shows them to be very recent... if it's not, then they're old images left over from something else.

```bash
$ docker image list
```

#### Start Redash locally, using the docker images you just built

```bash
$ make create_database
$ make up
```

The Redash web interface should also be available at http://localhost:5001, ready to be configured.

Once you've finished confirming everything works the way you want, then shut down the containers with:

```bash
$ make down
```
---

I've combined the relevant information from both parts, and you can continue from where you left off. Let me know if you need further assistance or modifications.
