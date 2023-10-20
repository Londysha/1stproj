from sqlalchemy import create_engine, text


db_connection_string = r"mysql+mysqlconnector://ydbgac2lqd3xb40kahg9:pscale_pw_qULClxP36B9J2uIjMaB1YXDhbVq9wHi2G054Ytf60NP@aws.connect.psdb.cloud/1stproj"

engine = create_engine(
  db_connection_string
)

# # Test if the database is connected by executing a simple SQL query
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT 1"))
#     print(result.fetchone())
