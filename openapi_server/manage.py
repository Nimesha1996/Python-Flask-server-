import sys
import os
sys.path.append(os.getcwd() + '/..')

from appConfig import db
from openapi_server.classes.db_model import *

db.create_all()
db.session.commit()
