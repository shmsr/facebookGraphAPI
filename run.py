#!/usr/bin/env python
from app import app, db

db.create_all()
app.run(host="127.0.0.1", port=8000, debug=True)