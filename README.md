# bookswitch
[![Dependency Status](https://david-dm.org/tomkoker/bookswitch.svg)](https://david-dm.org/tomkoker/bookswitch)
[![Code Climate](https://codeclimate.com/github/tomkoker/bookswitch/badges/gpa.svg)](https://codeclimate.com/github/tomkoker/bookswitch) 

## Author
[Tom Koker](http://tomkoker.com)

## Installing
Clone and change directory:
```bash
git clone https://github.com/tomkoker/bookswitch && cd bookswitch
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

[AGPL-3.0](https://github.com/tomkoker/bookswitch/blob/master/LICENSE)