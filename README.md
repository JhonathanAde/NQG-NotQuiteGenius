# Not Quite Genius (NQP)

Not Quite Genius is a one stop source for lyrics to your favorite songs.  


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

In order to run this application locally for testing purposes, Git, node.js (which comes with npm), and a database system (ie. Postgresql) is required. 


## Installing

```
# Clone this repository
$ git clone https://github.com/JhonathanAde/NQG-NotQuiteGenius.git
```
1. Create a database named nqg_app and an owner named nqg with a password
2. Create .env file at the root of this project, add environment variables provided in .env.example to .env file 
3. Set your database password as SECRET_KEY in .env file.

```
# Go into the repository, install backend dependencies at the root
$ pip install

# Go into react-app directory, install frontend dependencies 
$ npm install
```

### Running Application

```
# Run app from within react-app directory
$ npm start

# Go to root directory and run Flask
$ pipenv run flask run
```
Application should open up in your browser from localhost:3000


## Built With

* React - front-end
* Python (Flask SqlAlchemy, Alembic) = back-end
* Postgresql = database


## Contributing

1. Clone repo: $ git clone https://github.com/JhonathanAde/NQG-NotQuiteGenius.git
2. Create a new branch: $ git -b name_of_branch.
2. Make changes 
3. Submit Pull Request with description of changes


## Authors
* **Maximos Salzman** - https://github.com/Maximos-S
* **Scott Smith** - https://github.com/scottgit
* **Jhonathan Ade** - https://github.com/JhonathanAde
* **Andrew Choi** - https://github.com/achoi1225


## Acknowledgments

* App Academy for helping us develop the skills necessary to create this app.
