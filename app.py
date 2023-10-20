from flask import Flask, request
from flask import render_template
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from PIL import Image
# import base64
from db import engine
from sqlalchemy import  text

app = Flask(__name__)


@app.route("/")
def index():
    # Get the IP of the visitor
    ip = request.remote_addr
    #count = 0
    # Check if the IP is already in the database
    with engine.connect() as conn:
        conn.execute(text('''CREATE TABLE IF NOT EXISTS access
                 (ip TEXT, count INTEGER)'''))
        result = conn.execute(text("SELECT count FROM access WHERE ip={}".format(ip))).fetchone()

        if result is None:
            # If the IP is not in the database, insert it with a count of 1
            conn.execute(text("INSERT INTO access VALUES (?, ?)"),(ip, count))
            count = 1
        else:
            # If the IP is in the database, increment the count
            count = result[0] + 1
            conn.execute(text("UPDATE access SET count=? WHERE ip=?"), (count, ip))

        # Commit the changes to the database
        conn.commit()

    return f"Hello, your IP is {ip}. Total accessions: {count}"


























if __name__ == "__main__":
      app.run(host='0.0.0.0', debug=True)