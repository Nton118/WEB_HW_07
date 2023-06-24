from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
import pathlib

#  f'postgresql://username:password@domain_name:port/database_name'

file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

username = config.get('DEV_DB', 'user')
password = config.get('DEV_DB', 'password')
db_name = config.get('DEV_DB', 'db_name')
domain = config.get('DEV_DB', 'domain')
port = config.get('DEV_DB', 'port')

URL = f'postgresql://{username}:{password}@{domain}:port/{db_name}'

engine = create_engine(URL, echo=False, pool_size=5, max_overflow=0)
DBSession = sessionmaker(bind=engine)
session = DBSession()