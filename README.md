# Video Analytics Demo API

## Setup

### `pip install -r requirements.txt`

To run this project you will need to install all the dependencies use the above command to install it

## Running the development server

### `python manage.py migrate`

This will run all the database migrations.

### `python manage.py runserver`

Open [http://localhost:8000](http://localhost:8000) to view it in your browser.

## Create a superuser

### `python manage.py createsuperuser`

This commands creates a super for you which helps you login to the backend dashboard

Open [http://localhost:8000/admin/](http://localhost:8000/admin/) to view the backend admin.

[http://localhost:8000/admin/insight_data/event/](http://localhost:8000/admin/insight_data/event/) lists all the received data.

> :warning: **Dot Not Use in Production**: This backend application is not production ready.