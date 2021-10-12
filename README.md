# mollie_hackathons
Repo for mollie hackathons - private

# Hackathon 1: readme

This repo comes with a notebook containing an example of how to train a model called: `Training.ipynb`. Use this file to start the hackathon with. It will walk you through some steps that will result in a trained Random Forest model that can be used in different settings.

## Build an API

With the trained Random Forest model, you can create an API that has a `predict` endpoint. The endpoint will be waiting for data to make a prediction on. It makes this prediction by using the pretrained model. APIs are very commonly used interfaces between applications. They are used within mollie to connect merchants' websites to the mollie platform. APIs can communicate via a well defined protocol called HTTP. With this protocol, developers don't have to worrie about different languages or other differences between various applications.

## Wrap the API inside a Dockerfile

With docker we can easily contain the situation of small program within its own environment. We use it to make sure that the behaviour of the program is similar across platforms. Most cloud providers (AWS, Azure, GCS) work with containerised (Docker) images - as they are called. It is therefore useful for anyone to have some experience with Docker.