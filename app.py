from flask import Flask, request
from flask import render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from db import engine
from sqlalchemy import  text

app = Flask(__name__)


@app.route("/")
def index():
    # Get the IP of the visitor
    ip = request.remote_addr
    ip_parts = ip.split(".")
    ip_padded = ".".join([part.zfill(3) for part in ip_parts])
    ip = ip_padded.replace(".", "")
    # Check if the IP is already in the database
    with engine.connect() as conn:
        conn.execute(text('''CREATE TABLE IF NOT EXISTS access
                 (ip TEXT, count INTEGER)'''))
        result = conn.execute(text(f"SELECT count FROM access WHERE ip={ip}")).fetchone()

        if result is None:
            # If the IP is not in the database, insert it with a count of 1
            count = 1
            conn.execute(text(f"INSERT INTO access VALUES {ip, count}"))
            
        else:
            # If the IP is in the database, increment the count
            count = result[0] + 1
            conn.execute(text(f"UPDATE access SET count={count} WHERE ip={ip}"))

        # Commit the changes to the database
        conn.commit()
        counts=conn.execute(text(f"SELECT SUM(count) FROM access")).fetchone()[0]
              
    ip_display = ".".join([ip[:3], ip[3:6], ip[6:9], ip[9:]]) # Display the IP with dots
    return f"Hello, your IP is {ip_display}. Total accessions: {counts}"
    


























if __name__ == "__main__":
      app.run(host='0.0.0.0', debug=True)