# Colonize And Conquer

## Technology Stack
  - Django
  - Python
  - Vue.js
  - JavaScript
  - HTML
  - CSS
  - FontAwesome
  - Bootstrap

### Installation

Install the dependencies and start the server.

```sh
$ cd colonize-and-conquer
$ pip install -r requirements.txt
$ python manage.py makemigrations alliance, cityMap, kontakt, mainPage, messagess, premium, profileUser, rankings, raports, scheduleTasks, worldMap
$ python manage.py migrate
$ python manage.py runserver
```
### Installation gcloud shell

```sh
$ cd colonize-and-conquer
$ pip install -r requirements.txt
$ ./cloud_sql_proxy -instances=solwit-pjatk-arc-2018-gr1:europe-west1:test1=tcp:3306
$ python manage.py makemigrations alliance, cityMap, kontakt, mainPage, messagess, premium, profileUser, rankings, raports, scheduleTasks, worldMap
$ python manage.py migrate
$ python manage.py runserver
```

