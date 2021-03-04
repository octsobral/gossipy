import uuid
from datetime import datetime

import mongoengine as mongo


class News(mongo.Document):

    id = mongo.UUIDField(primary_key=True, default=uuid.uuid4)
    source = mongo.StringField(required=True)
    query = mongo.StringField(required=True)
    title = mongo.StringField(required=True)
    url = mongo.StringField(required=True)
    published_at = mongo.StringField(required=True, editable=False)
    timestamp = mongo.DateTimeField(required=True, default=datetime.utcnow, editable=False)
    hash = mongo.StringField(required=True, editable=False)
