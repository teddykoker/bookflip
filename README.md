# bookswitch
## Author
[Tom Koker](http://tomkoker.com)

## Run Locally
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
webpack --watch
python run.py
```
