# CS362-CryptoCurrencyViewer
A Dynamic Web App built on HTML, CSS and Flask to display current cryptocurrency prices, and data.

Users can also create accounts and maintain a portfolio.

---

## Instructions(For Group):

1. It's **HIGHLY** recommended to have a virtualenv running, when setting up the packages and enviroment for this project. More info about getting and setting up a virtualenv can be found  [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/#lower-level-virtualenv).

2. Install packages on python with the command:
  ``` py
    pip install -r requirements.txt
  ```

3. Run virtualenv:
``` BASH
source {nameofvirtualenv}/bin/activate
```
Note the {nameofvirtualenv} is the one you chose, and does not include {}.

3. Set a FLASK_APP enviroment variable, so the flask app knows where to run:
``` BASH
export FLASK_APP=run.py
```

4. Run the server!
``` BASH
flask run
```

## Resources (For Group):
[Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
  * This source is **REALLY** useful. It provides a ton of info and tutorials on backend programming on flask.
[Flask-SQLAlchemy Documentation](http://flask-sqlalchemy.pocoo.org/2.3/)
  * Documentation for SQLAlchemy. 
