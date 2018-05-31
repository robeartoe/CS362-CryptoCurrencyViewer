# CS362-CryptoCurrencyViewer
A Dynamic Web App built on HTML, CSS and Flask to display current cryptocurrency prices, and data.

Users can also create accounts and maintain a portfolio.

---
## Screenshots:
![](https://github.com/robeartoe/CS362-CryptoCurrencyViewer/blob/master/Images/mainPage.png)
![](https://github.com/robeartoe/CS362-CryptoCurrencyViewer/blob/master/Images/currency.png)
![](https://github.com/robeartoe/CS362-CryptoCurrencyViewer/blob/master/Images/user2.png)

## Frameworks Used:
HTML, CSS, Flask, JQuery,Ajax, and SqlAlchemy.

## Installation:

1. It's **HIGHLY** recommended to have a virtualenv running, when setting up the packages and enviroment for this project. More info about getting and setting up a virtualenv can be found  [here](http://docs.python-guide.org/en/latest/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more) .

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

## Credits:
This project wouldn't have been made possible without the help of John Nguyen, and Fares Alfowzan. 

## License:
This project is created under the MIT License. 
