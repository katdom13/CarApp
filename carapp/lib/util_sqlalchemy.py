import datetime
import uuid
from sqlalchemy import DateTime
from sqlalchemy.types import TypeDecorator
from carapp.extensions import db
from lib.util_datetime import tzware_datetime

class AwareDateTime(TypeDecorator):
  impl = DateTime(timezone=True)

  def process_bind_param(self, value, dialect):
    # if isinstance(value, datetime.datetime) and value.tzinfo is None:
    #   raise ValueError('{!r} must be TZ-aware'.format(value))
    
    return value

class ResourceMixin(object):
  create_date = db.Column(AwareDateTime(), default=tzware_datetime)

  update_date = db.Column(AwareDateTime(), default=tzware_datetime)

  @classmethod
  def sort_by(cls, field, direction):
    if field not in cls.__table__.columns:
      field = 'create_date'
    
    if direction not in ('asc', 'desc'):
      direction = 'asc'

    return field, direction

  @classmethod
  def generate_random_id(cls):
    return uuid.uuid4().hex

  def save(self):
    db.session.add(self)
    db.session.commit()

    return self
  
  def delete(self):
    db.session.delete(self)
    return db.session.commit()