from . import db
from datetime import datetime
import json

class Endpoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    path = db.Column(db.String(300), nullable=False)
    method = db.Column(db.String(10), nullable=False, default='POST')
    query_schema = db.Column(db.Text, default='{}')
    body_schema = db.Column(db.Text, default='{}')
    response_schema = db.Column(db.Text, default='{}')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def query_schema_dict(self):
        try: return json.loads(self.query_schema)
        except: return {}

    def body_schema_dict(self):
        try: return json.loads(self.body_schema)
        except: return {}

    def response_schema_dict(self):
        try: return json.loads(self.response_schema)
        except: return {}
