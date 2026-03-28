from flask import Flask, request, jsonify,render_template
import psutil

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")


@app.get("/metrics")
def get_metrics():
        cpu_percentage = psutil.cpu_percent(interval=1)
        memory_percentage = psutil.virtual_memory().percent
        disk_usage= psutil.disk_usage("/")
        net_io_stat=psutil.net_io_counters()


        return jsonify({
            "cpu_percentage": cpu_percentage,
            "memory_percentage": memory_percentage,
            "disk_used_gb": round(disk_usage.used / 1e9, 2),
            "disk_total_gb": round(disk_usage.total / 1e9, 2),
            "bytes_sent": round(net_io_stat.bytes_sent/1e9,2),
            "bytes_recv": round(net_io_stat.bytes_recv/1e9,2)
        }), 200
    
    


app.run(debug=True)