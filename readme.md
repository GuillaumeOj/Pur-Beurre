# Contents page
- [I. What is PurBeurre?](#i-what-is-purbeurre)
- [II. How to install?](#ii-how-to-install)
- [III. How to use?](#iii-how-to-use)
- [IV. To do list](#iv-to-do-list)
- [V. Technologies and ressources](#v-technologies-and-ressources)

# I. What is PurBeurre?
[⇧ *Top*](#contents-page)
The aim of this application is to propose a substitute for a food product.
The application use the open database provide by the [Open Food Facts](https://world.openfoodfacts.org/).
This application is made for the project 8 from [OpenClassrooms'](https://openclassrooms.com/fr/paths/68/projects/159/assignment) Python course.

The application is alive here => http://projet-8.ojardias.io

# II. How to install?
[⇧ *Top*](#contents-page)
To install this project on your computer you need **SQLite3** and **Python3**.

First clone this repository using:
```
git@github.com:GuillaumeOj/Pur-Beurre.git
or
https://github.com/GuillaumeOj/Pur-Beurre.git
```

Then create your virtual environnement and install the dependencies.
You can use **Poetry** or just **virtualenv** and **pip**.

You're ready to run the application!

# III. How to use?
[⇧ *Top*](#contents-page)
At the first start of the application you need to create and populate the database.

For creating the database, run:
```
python manage.py migrate
```

For populating the database, run:
```
python manage.py init_db
```

Now, to start the server, run:
```
python manage.py runserver
```

# IV. To do list
[⇧ *Top*](#contents-page)

See my [Trello](https://trello.com/b/TWtodZpE/purbeurre)

# V. Technologies and ressources
[⇧ *Top*](#contents-page)

This application use various technologies and ressources.

- Main language  => [Python 3.8](https://www.python.org/)
- Framework => [Django](https://www.djangoproject.com/)
- Template => [Creative from Start Bootstrap](https://startbootstrap.com/themes/creative/)
