# Thundershare ⚡ Share files over your LAN with ease

## What problem does this project solve?

Ever notice how the quickest way to send a file or some text from your mobile phone
to your computer is often to e-mail it to yourself?
In this day an age, how ridiculous!

Thundershare lets you send files over a home network with ease.
Simply navigate to `<ip of machine running the app>:8000`
to upload and download files you want shared locally.

Files never leave the host machine - sleep soundly
knowing your files are safe.

## Usage

### Requirements

[`make`](https://www.gnu.org/software/make/) and [`docker`](https://docs.docker.com/engine/install/)

### Installation instructions

Clone this repo, then run:

```
# build app
make build

# run app
make run

# access the app at <machine ip>:8000
```
