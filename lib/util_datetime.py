import datetime
import pytz

def tzware_datetime():
  return datetime.datetime.now(pytz.utc)