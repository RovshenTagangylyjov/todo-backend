# Todo Backend

**Make sure that you have python setup that can be referenced with command python to easily follow the tutorial. If your python is referenced with python, then replace all pythons with python**

## Install Docker

### For Linux

```
sudo apt install -y \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
                "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
                $(lsb_release -cs) \
                stable"

sudo apt update && sudo apt upgrade

sudo apt install -y docker-ce docker-ce-cli containerd.io

sudo usermod -aG docker "$USER"
```

### For Windows

Follow the steps [here](https://docs.docker.com/docker-for-windows/install/)

## Download postgres image and run it with Docker

### For Linux

```
sudo apt update && sudo apt upgrade
sudo apt install python-pip python-dev libpq-dev
docker run -d --name postgres --restart always -p 127.0.0.1:5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=todo postgres
```

### For Windows

```
python -m pip install --upgrade pip
docker run -d --name postgres --restart always -p 127.0.0.1:5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres postgres -e POSTGRES_DB=todo
```

**Your terminal must be in the root of the backend folder for all the commands below !!**

## Install Poetry

### For Linux

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### For Windows

```
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

## Install Dependencies

> **Note: If you have incompatible python version, you can install [pyenv](https://github.com/pyenv/pyenv) to manage python versions!**

### Activate venv

```
poetry shell
```

### Install packages

```
poetry install
```

### Add a new dependency

```
poetry add package_name
```

### Remove a dependency

```
poetry remove package_name
```

> **IMPORTANT: Do not forget to run `poetry lock` command before committing!**

## Activate pre-commit

### Set pre-commit to run automatically before commits

`pre-commit install`

### (optional) Manually format files

`pre-commit run --all`

## Migrate

```
python manage.py migrate
```

## Create superuser

```
python manage.py createsuperuser
```

## Runserver

```
python manage.py runserver
```
