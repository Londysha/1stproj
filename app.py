from flask import Flask
from flask import render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import base64

app = Flask(__name__)

@app.route("/")
def index():
    series = pd.Series([1, 3, 5, np.nan, 6, 8])
    figuer = plt.figure()
    ax = figuer.add_subplot(1, 1, 1)
    ax.plot(series)
    plt.savefig(r'./static/images/fig.png')
    
    fig=Image.open(r"./static/images/fig.png")
     # Convert the image to base64
    image_data = fig.tobytes()
    base64_image = base64.b64encode(image_data).decode('utf-8')

    return render_template("home.html", fig=base64_image)
























if __name__ == "__main__":
      app.run(host='0.0.0.0', debug=True)