from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para cualquier origen
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("connect")
def handle_connect():
    print("Cliente conectado.")

@socketio.on("disconnect")
def handle_disconnect():
    print("Cliente desconectado.")

@socketio.on("command")
def handle_command(data):
    print(f"Comando recibido: {data}")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
