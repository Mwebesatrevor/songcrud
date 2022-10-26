
#  MUSICAPP
This is a simple musicapp API. It is built using Django and Django Rest Framework.


## Why I created MUSICAPP
Just for practise.

## Development Setup

We use `pipenv` to manage our dependencies. To install `pipenv` run the following command:

    pip install pipenv

Clone the repository by running the following command in your terminal:
```
git clone https://github.com/Mwebesatrevor/songcrud.git
```

Create a Python virtual environment 

```
pipenv shell

```

Install the dependencies by running the following command in your terminal:
```
pipenv install 

```

Create .env file following the .env_example file

```
cp .env_example .env

```

Run migrations
```
python manage.py make migrations
python manage.py migrate

```

- Run application
```
python manage.py runserver

```

. 
## Run tests
```
pytest

```

## Credits
Musicapp is designed and built by Mwebesa Trevor
 



