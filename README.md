# bookflip
[![Dependency Status](https://david-dm.org/tomkoker/bookflip.svg)](https://david-dm.org/tomkoker/bookflip)
[![Code Climate](https://codeclimate.com/github/tomkoker/bookflip/badges/gpa.svg)](https://codeclimate.com/github/tomkoker/bookflip) 

## Author
[Tom Koker](http://tomkoker.com)

## Installing
Clone and change directory:
```bash
git clone https://github.com/tomkoker/bookflip && cd bookflip
```

Create python virtual environment:
```bash
virtualenv venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
npm install
```

Initialize database:
```bash
python
>>> from server import db
>>> db.init_db()
>>> quit()
```

Build and start the server:
```bash
webpack
python run.py
```

## License

[AGPL-3.0](https://github.com/tomkoker/bookflip/blob/master/LICENSE)