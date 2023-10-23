from sqlalchemy import create_engine, text


db_connection_string = r"mysql+mysqlconnector://z88yw70413ox79nw4hle:pscale_pw_JiVnVY6IPQ4JOwMmXA2rtpIguXu9bI1RzUAnrweX1X8@aws.connect.psdb.cloud/1stproj"

engine = create_engine(
  db_connection_string
)

# # Test if the database is connected by executing a simple SQL query
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT 1"))
#     print(result.fetchone())
