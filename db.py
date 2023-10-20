from sqlalchemy import create_engine, text


db_connection_string = r"mysql+mysqlconnector://trtarkdcq4kinjh6m6zj:pscale_pw_vsBXwT9yA1gqESwFoKDQxJSRF2H2t7HnVMXuaFuR4rv@aws.connect.psdb.cloud/1stproj"

engine = create_engine(
  db_connection_string
)

# # Test if the database is connected by executing a simple SQL query
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT 1"))
#     print(result.fetchone())
