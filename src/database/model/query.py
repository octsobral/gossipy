import uuid
from datetime import datetime

import mongoengine as mongo


class Query(mongo.Document):

    id = mongo.UUIDField(primary_key=True, default=uuid.uuid4)
    name = mongo.StringField(required=True)
    timestamp = mongo.DateTimeField(required=True, default=datetime.utcnow, editable=False)