# Weather API Pipeline

## Project Overview

Weather API Pipeline is a real-time weather monitoring system built using Python. The project fetches weather data from the OpenWeather API, stores it in a PostgreSQL database, and displays the data through an interactive Streamlit dashboard.

The system automatically collects weather information for multiple cities using a background scheduler and maintains historical weather records for analysis and visualization.

---

## Features

* Real-time weather data collection
* Multi-city weather monitoring
* PostgreSQL database integration
* SQLAlchemy ORM for database operations
* Alembic database migrations
* APScheduler for automated data collection
* Streamlit dashboard for visualization
* Auto-refresh dashboard
* Historical weather tracking
* Temperature and humidity trend analysis

---

## Technology Stack

* Python
* PostgreSQL
* SQLAlchemy
* Alembic
* APScheduler
* Streamlit
* Pandas
* Requests
* OpenWeather API

---

## Project Architecture

OpenWeather API
↓
Weather Service (Extract)
↓
Data Transformation
↓
PostgreSQL Database (Load)
↓
Streamlit Dashboard (Visualization)

---

## ETL Workflow

### Extract

Weather data is fetched from the OpenWeather API.

### Transform

Relevant fields such as city, temperature, humidity, weather condition, and timestamp are extracted from the API response.

### Load

Processed data is stored in PostgreSQL using SQLAlchemy ORM.

---

## Database Schema

Table: weather_data

| Column      | Type     |
| ----------- | -------- |
| id          | Integer  |
| city        | String   |
| temperature | Float    |
| humidity    | Integer  |
| weather     | String   |
| fetched_at  | DateTime |

---

## Scheduler

APScheduler runs as a background process and automatically fetches weather data every 10 minutes for multiple cities:

* Ahmedabad
* Mumbai
* Delhi
* Bangalore
* Surat
* Pune
* Hyderabad

---

## Dashboard Features

* City-wise filtering
* Current weather metrics
* Temperature trend chart
* Humidity trend chart
* Average temperature comparison
* Historical weather records
* Auto-refresh functionality

---

## Installation

### Clone Repository

git clone <repository_url>

cd weather-api-pipeline

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

Windows:

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

---

## Environment Variables

Create a `.env` file in the project root:

DB_USER=postgres

DB_PASSWORD=your_password

DB_HOST=localhost

DB_PORT=5432

DB_NAME=weather_db

API_KEY=your_openweather_api_key

---

## Run Scheduler

python -m scheduler.weather_scheduler

---

## Run Dashboard

streamlit run dashboard/streamlit_app.py

---

## Learning Outcomes

This project demonstrates:

* ETL Pipeline Development
* API Integration
* PostgreSQL Database Management
* SQLAlchemy ORM
* Database Migrations using Alembic
* Background Job Scheduling
* Data Visualization using Streamlit
* Real-Time Monitoring Systems

---

## Author

Smit Patel
