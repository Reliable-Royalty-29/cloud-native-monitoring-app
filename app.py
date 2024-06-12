import psutil
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    cpu_parcentage = psutil.cpu_percent()
    memory_parcentage = psutil.virtual_memory().percent
    message = None
    if cpu_parcentage > 80 or memory_parcentage > 80:
        message = "High CPU or Memory Utilization Detected. Please check and scale up"
    return render_template("index.html", cpu_metric=  cpu_parcentage,  mem_metric= memory_parcentage, message= message)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')   
