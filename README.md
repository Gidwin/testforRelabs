# Тестовое задание для Relabs

#### Installation

git clone:

```sh
git@github.com:Gidwin/testforRelabs.git:
```

Change to the project directory::

```sh
cd testforRelabs/
```

Create a virtual environment:

```sh
python -m venv venv
```

Activate the virtual environment:

```sh
source venv/scripts/activate
```

Install the dependencies:

```sh
pip install -r requirements.txt
```
#### Usage

Start the server

```sh
c папки task/ uvicorn main:app --reload

```

Open:

```sh
http://127.0.0.1:8000/
```
