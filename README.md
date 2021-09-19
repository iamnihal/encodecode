<h1 align="center">EncoDecoder: A Web Utitliy to Encode/Decode various schemes</h1>

[![version](https://img.shields.io/badge/version-1.0-red)](https://www.github.com/iamnihal/encodecode)
[![python](https://img.shields.io/badge/python-3.8.1-blue.svg?logo=python&labelColor=yellow)](https://www.python.org/downloads/)
[![django](https://img.shields.io/badge/django-3.2.6-blue.svg?logo=django&labelColor=grey)](https://www.python.org/downloads/)
[![platform](https://img.shields.io/badge/platform-osx%2Flinux%2Fwindows-green.svg)](https://github.com/iamnihal/encodecode/)
  <br />
```
It contains the following utilities:-
- URL Encoding/Decoding 
- Base64 Encoding/Decoding
- HTML Entities Encoding/Decoding
- Generate and Decrypt MD5 hashes.
- Generate SHA-1, SHA-256, SHA-512.
- JSON Prettifier & CSP Evaluator.
```
## Demo: [Live](https://encodeapp.herokuapp.com)

![Preview](https://user-images.githubusercontent.com/37813784/133926608-1c6aef1a-d1ae-4e2c-90c4-6fc817c9d31c.png)

### Installation

1) Create a virtualenv:
```
$ python3 -m venv <virtual env path>
```
2) Activate the virtualenv you have just created:
```
$ source <virtual env path>/bin/activate
```
3) Clone this repository:
```
$ git clone https://github.com/iamnihal/encodecode.git
````
4) Install the requirements:
```
$ pip install -r requirements.txt
```
5) Apply migrations:
```
$ python manage.py migrate
```
6) Run the server:
```
$ python manage.py runserver
```

and load the app at http://127.0.0.1:8000


> :warning: Warning:-  **Change SECRET_KEY in settings.py for the security purpose. To generate your own SECRET_KEY, use this:-**
```
python -c "import secrets; print(secrets.token_urlsafe())"
```

<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

