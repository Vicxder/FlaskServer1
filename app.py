from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS
import eventlet

# Inicializar Flask y Flask-SocketIO
app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir conexiones de diferentes dominios
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

# Ruta para servir la página principal
@app.route("/")
def index():
    return render_template("index.html")

# Manejo de la conexión de WebSocket
@socketio.on("connect")
def handle_connect():
    print("Cliente conectado.")

# Manejo de la desconexión de WebSocket
@socketio.on("disconnect")
def handle_disconnect():
    print("Cliente desconectado.")

# Manejo de comandos enviados desde el cliente
@socketio.on("command")
def handle_command(data):
    print(f"Comando recibido: {data}")

# Ejecutar el servidor en el puerto proporcionado por Render
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Usar el puerto asignado por Render
    socketio.run(app, host="0.0.0.0", port=port, debug=True)
