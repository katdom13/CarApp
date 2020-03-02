from collections import OrderedDict
from sqlalchemy import or_
from carapp.lib.util_sqlalchemy import ResourceMixin
from carapp.extensions import db, ma
from carapp.lib.constants import(
  SHORT_STRING,
  MEDIUM_STRING
)

class Car(ResourceMixin, db.Model):
  
  COLOR = OrderedDict([
    ('blue', 'Blue'),
    ('red', 'Red')
  ])

  __tablename__ = 'car'

  id = db.Column(db.String(MEDIUM_STRING), primary_key=True)
  name = db.Column(db.String(SHORT_STRING), nullable=False)
  color = db.Column(db.Enum(*COLOR, name='color', native_enum=False), index=True, nullable=False, server_default='blue')

  def __init__(self, **kwargs):
    # Call Flask-SQLAlchemy's constructor
    super(Car, self).__init__(**kwargs)

    self.id = Car.generate_random_id()
    
  @classmethod
  def find_by_identity(cls, identity):
    """
    Find a car by their name or colo

    :param identity: name or color
    :type identity: str
    :return: Car instance
    """
    return Car.query.filter((cls.id == identity)
      | (cls.name == identity)
      | (cls.color == identity)).first()

  @classmethod
  def search(cls, query):
    if not query:
      return ''
    
    query = '%{0}%'.format(query)
    fields = (cls.name.ilike(query),
      cls.color.ilike(query)
    )

    return or_(*fields)

  def to_dict(self, decode=False):
    """
    Returns a dictionary containing all the car fields as key-word arguments.
  
    :param decode: Foreign IDs are shown as name strings instead of hash strings.
    :type decode: bool
    :return: dict
    """
    schema = CarSchema()
    _dict = schema.dump(self)
    
    return _dict

class CarSchema(ma.ModelSchema):
  class Meta:
    include_fk = True
    model = Car