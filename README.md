# Sensor Simulation Project Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Services Overview](#services-overview)
4. [API Usage](#api-usage)
5. [Design Choices](#design-choices)
6. [Challenges and Solutions](#challenges-and-solutions)
7. [Learning Experience](#learning-experience)
## Introduction

Welcome to the documentation for the Sensor Simulation project. This project aims to simulate sensor behavior, monitor readings, and provide APIs for data retrieval based on specific criteria. This document provides instructions for setting up and interacting with the system, an overview of the services, insights into design choices, discussions about challenges faced during development, and a reflection on the learning experience gained from this project.

## Getting Started

### System Setup

To set up and interact with the system, follow these steps:

- Install Docker on your machine if not already installed.
- Clone this repository: `https://github.com/SoumavaBiswas/sensor-simulation.git`
- Navigate to the project folder: `cd sensor-simulation`
- Start the system using Docker Compose: `docker-compose up -d`
- Access the FastAPI endpoints at `http://localhost:8000`

### Interacting with the System
- The MQTT publisher simulates sensor readings and publishes them to topics like sensors/temperature and sensors/humidity.
- The MQTT subscriber captures these readings and stores them in a MongoDB collection. Latest ten sensor readings are also stored in Redis for quick access.
- The FastAPI application exposes endpoints to retrieve sensor data based on criteria.
- Access the FastAPI endpoints using a web browser or tools like cURL or Postman. More details are provided in the API Usage section of this document.

## Services Overview
The project is composed of the following services, each serving a specific purpose:

- Mosquitto MQTT Broker: Provides a messaging platform for sensor readings.
- MQTT Publisher: Simulates multiple sensor readings and publishes them to MQTT topics.
- MQTT Subscriber: Captures MQTT messages and stores them in a MongoDB collection.
- MongoDB: Stores the sensor readings data.
- Redis: Stores the latest ten sensor readings for quick retrieval.
- FastAPI: Exposes endpoints to retrieve sensor readings.

Refer to the docker-compose.yml file for a detailed configuration of each service.

## API Usage
The FastAPI application provides endpoints to retrieve sensor readings based on specific criteria.

### Retrieve Sensor Readings

**Endpoint:** `/sensor_readings`

**HTTP Method:** GET

**Parameters:**
- `start` (optional): Start timestamp in ISO 8601 format (default: None).
- `end` (optional): End timestamp in ISO 8601 format (default: None).

**Response:**
- Returns a list of sensor readings within the specified time range.
- Returns sensor readings for last 1 hour, if no parameter is given.
- Returns error message if provided timestamp is not in ISO 8601 format.

### Retrieve Latest Sensor Readings

**Endpoint:** `/latest_readings`

**HTTP Method:** GET

**Response:**
- Returns a list of latest ten sensor readings.

## Design Choices
Throughout the project, specific design choices were made to enhance performance, maintainability, and scalability. For instance:

- Docker was chosen to ensure consistent environments across development and deployment.
- MQTT was selected for its lightweight publish-subscribe messaging pattern.
- MongoDB was employed for persistent data storage.
- Redis was used to cache the latest sensor readings and improve retrieval speed.

## Challenges and Solutions

- ### Handling Simulated Data

Challenge: Generating meaningful simulated sensor data.

Solution: Used random number generation within relevant ranges to simulate sensor readings.

- ### User Input Validation

Challenge: Validating user input for ISO8601-formatted dates in the API endpoints.

Solution: Implemented input validation in the FastAPI app by checking for proper ISO8601 format using libraries like dateutil.parser

- ### Data Consistency

Challenge: Ensuring data consistency between MQTT subscriber and MongoDB.

Solution: Implemented appropriate error handling and retries in the MQTT subscriber.

- ### Scalability

Challenge: Designing for potential scalability.

Solution: Docker Compose allows easy replication of services, and Redis cache aids in handling larger datasets.

## Learning Experience

During the development of this project, I encountered various challenges and gained valuable knowledge, especially considering that I had no prior experience with MQTT. Here are some key takeaways and learning experiences:

- ### Exploring MQTT

As someone without prior knowledge of MQTT (Message Queuing Telemetry Transport), diving into the world of MQTT was a learning curve. I had to understand the concepts of topics, brokers, and clients. The MQTT protocol's publish-subscribe architecture opened up new ways of thinking about real-time data communication.

- ### Setting Up the MQTT Broker

One of the initial challenges was setting up the Mosquitto MQTT broker using Docker. It involved understanding Docker concepts, network configurations, and ensuring the broker's proper functioning.

- ### Building Python MQTT Clients

Creating both the MQTT publisher and subscriber from scratch in Python required learning the Paho MQTT library. This involved grasping how to establish connections, publish messages, and handle incoming messages.
