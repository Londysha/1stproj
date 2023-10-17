from sqlalchemy import create_engine, text
#import os


DB_HOST=aws.connect.psdb.cloud
DB_USERNAME=yenrtgws1jzkgavb6jax
DB_PASSWORD=************
DB_NAME=davidliuwebappdatabase
db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })