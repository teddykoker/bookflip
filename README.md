# bookswitch
## Author
[Tom Koker](http://tomkoker.com)

## Run Locally
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
