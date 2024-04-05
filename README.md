# Take Home Assesment

## Purpose

This application is designed to visualize the number of revisions made to a Wikipedia page in relation to a specific event stored in our database. By plotting these revisions over time, we aim to analyze whether a particular event correlates with significant changes to a relevant Wikipedia page.

## How It Works

1. Input: Users select an event from the database and provide a list of Wikipedia page titles they wish to analyze.
2. Data Retrieval: The application retrieves revision data for the specified Wikipedia pages from the Wikipedia API.
3. Visualization: The number of revisions for each Wikipedia page is plotted over time using a histogram.
4. Analysis: Users can visually examine the revision trends and assess whether the selected event correlates with notable changes to the Wikipedia pages.

Features
- Selection of events from the database
- Input of Wikipedia page titles for analysis
- Visualization of revision data using interactive charts
- Hypothesis testing regarding event impact on Wikipedia content

## Setup

1. After Completeing the initial steps provided in the `README.md` file. We need to populate or database with the provided CSV file
2. Navigate to the `django-base-main` directory using `cd django-base-main`. Then run the command `poetry run python manage.py upload_data` to import data from CSV file.
3. Navigate to `django-base-main` directory to start the project and then execute `poetry run python manage.py runserver`.

## Dependencies

- Python
- Django framework
- Requests
