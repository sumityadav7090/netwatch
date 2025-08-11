from flask import Flask, render_template, jsonify
from packet_capture import get_packets, start_capture
import threading

app = Flask(__name__)

# Start packet capture in background thread
capture_thread = threading.Thread(target=start_capture)
capture_thread.daemon = True
capture_thread.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/packets')
def packet_data():
    # Get the captured packets and return as JSON
    packets = get_packets()
    return jsonify(packets)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
