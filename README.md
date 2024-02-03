# Tanxfi Task

## Description
This project is a Django application for managing price alerts for cryptocurrencies.

## Setup
Follow these steps to set up and run the project:

### Open the terminal and navigate to the project directory and run this command

Install the honcho library using this command


### **pip install honcho**


and run this command to start the django api and background tasks

### **honcho start**

If that doesn't work


## open the project file in the terminal and run these commands



- *pip install -r requirements.txt*

- *python manage.py makemigrations*

- *python manage.py migrate*

- *python manage.py runserver*

- Run these commands in different terminals from now

- *celery -A tanxfi_task beat -l info*

- *celery -A tanxfi_task worker -l info*




This will start the Django development server and the background tasks worker(Redis, Celery).

to stop this just press ctrl+c

you can access the api's in the web browser using this url

url : http://127.0.0.1:8000/alerts/create/




## END-POINTS

- http://127.0.0.1:8000/alerts/create/ - For creating the alerts here you can add the crypto_currency and target_price

- http://127.0.0.1:8000/alerts/delete/{id}/ - We can delete the alerts that are created before

- http://127.0.0.1:8000/alerts/list/ - We can access all the alerts that are created before

- http://127.0.0.1:8000/token/ - Here we can create the JWT token to access the API

  and also there is no user creation functionality in this code a django super user has been created 

  with user name surya and password 001

  using this you can create the access token and refresh token

- http://127.0.0.1:8000/token/refresh/ - Here using the refresh token we had before we can get the new access token





## Project overview

In this application I used django rest frame work to build a api which continously checks the bitcoin price and also this api allows the users to create, delete and see the list of all the alerts they have created. I used inbuilt sqlite database for this api and used the api which was provided in the task details file and used it to monitor the bitcoin price and created the functionality which sends email to the user when the alert has been triggered. Here I used celery and redis which I used for the background tasks. I have used the honcho for running all the tasks at once.

To test the api start the api and run the commands in testing.ipynb