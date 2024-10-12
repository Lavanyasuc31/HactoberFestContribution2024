# Django Job Alert Project

This Django-based web application helps users find jobs that match their preferences and sends email notifications when new jobs are available. The project utilizes Celery workers to scrape job websites, with job notifications handled asynchronously, outside of the typical request-response cycle. Celery Beat runs scheduled tasks every 5 minute to check for new jobs.

## Features
- User profile creation: Collects details like username, age, phone number, preferred job type, location, and title.
- Job scraping: Scrapes jobs from external job websites based on user preferences.
- Email notifications: Sends emails when a job matching the user’s preferences is found.
- Asynchronous processing: Powered by Celery and Redis, job scraping and notifications are handled without blocking the user interface.
- Celery Beat: Runs scheduled tasks every 5 minute to look for new jobs.

## Prerequisites

Make sure the following are installed on your machine:
- [PostgreSQL](https://www.postgresql.org/) (for database)
- [Redis](https://redis.io/) (for task queuing with Celery)

## Installation 
Open the folder in your preferred IDE and run the following 6 command in 4 seprate terminals
Note: **it is preferred to creta a virtual environment first** <br>
1.0) pip install -r requirements.txt (Install dependencies) <br>
1.1) python manage.py migrate (Update your settings.py with the PostgreSQL credentials, then run) <br>
1.2) python manage.py runserver (Run the Django development server) <br>
2) redis-server (Start Redis Server) <br>
3) celery -A job_alert_core worker --pool=solo -l info (Run Celery Worker) <br>
4) celery -A job_alert_core beat -l info (Run Celery Beat Scheduler) <br>

That's it! Access the web app at the URL provided by the Django development server (usually http://127.0.0.1:8000).

