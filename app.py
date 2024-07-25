from flask import Flask, jsonify, render_template
import psutil
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/metrics')
def metrics():
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    memory = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)
    disk = psutil.disk_usage('/')
    network = psutil.net_io_counters()

    data = {
        'uptime': uptime.total_seconds(),
        'memory': {
            'total': memory.total,
            'used': memory.used,
            'free': memory.free,
            'percent': memory.percent
        },
        'cpu': cpu,
        'disk': {
            'total': disk.total,
            'used': disk.used,
            'free': disk.free,
            'percent': disk.percent
        },
        'network': {
            'bytes_sent': network.bytes_sent,
            'bytes_recv': network.bytes_recv
        }
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

