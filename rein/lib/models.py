from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user import Base
import os
import logging

log = logging.getLogger('python-rein')

config_dir = os.path.join(os.path.expanduser('~'), '.rein')
db_filename = 'local.db'
if not os.path.isdir(config_dir):
    os.mkdir(config_dir)

engine = create_engine("sqlite:///%s" % os.path.join(config_dir, db_filename))
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
log.info('database connected')

Base.metadata.create_all(engine)

from bucket import Base
Base.metadata.create_all(engine)

from order import Base
Base.metadata.create_all(engine)

from placement import Base
Base.metadata.create_all(engine)

from document import Base
Base.metadata.create_all(engine)

from persistconfig import Base
Base.metadata.create_all(engine)

log.info('database tables updated')
