## Overview

This Flask application contains the basic CRUD item functionality to demonstrate the use of pytest.

## How to Run

In the top-level directory:

    $ export FLASK_APP=app.py
    $ export FLASK_ENV=development
    $ flask run

## Installation Instructions

Pull down the source code from this Github repository:

```sh
git clone git@github.com:sujala/Rady_SDET_Technical.git```

Create a new virtual environment:

```sh
$ cd Rady_SDET_Technical
$ python3 -m venv venv
```

Activate the virtual environment:

```sh
$ source venv/bin/activate
```

Install the python packages in requirements.txt:

```sh
(venv) $ pip install -r requirements.txt
```

Set the file that contains the Flask application and specify that the development environment should be used:

```sh
(venv) $ export FLASK_APP=app.py
(venv) $ export FLASK_ENV=development
```

Run development server to serve the Flask application:

```sh
(venv) $ flask run
```

## Key Python Modules Used

- Flask: micro-framework for web application development
- flask_sqlalchemy - ORM (Object Relational Mapper)
- Pytest

This application is written using Python 3.8.5.

## Testing

```sh
(venv) $ pytest -v
```
