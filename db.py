from sqlalchemy import create_engine, text


db_connection_string = r"mysql+mysqlconnector://xzxvku8wlo5ti70zxv3r:pscale_pw_f37kNG2LD4cGbVZYZqXfRoU2k8gDM79b7M7tEym3MBX@aws.connect.psdb.cloud/1stproj"

engine = create_engine(
  db_connection_string
)

# Test if the database is connected by executing a simple SQL query
with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.fetchone())
