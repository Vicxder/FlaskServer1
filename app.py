from flask import Flask, request, send_from_directory
from flask_cors import CORS
from flask_socketio import SocketIO, emit

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configuración de CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# Configuración de SocketIO con soporte para WebSockets
socketio = SocketIO(app, cors_allowed_origins="*")

# Ruta para servir la página index.html
@app.route("/")
def index():
    return send_from_directory(".", "index.html")  # Sirve index.html desde el directorio actual

# Rutas para otros archivos estáticos (CSS, JS, imágenes)
@app.route("/<path:path>")
def serve_static_file(path):
    return send_from_directory(".", path)

# Eventos de WebSocket
@socketio.on("connect")
def handle_connect():
    """
    Manejo de conexión de un cliente.
    """
    print("Cliente conectado.")
    emit("server_response", {"message": "Conexión establecida con el servidor Flask."})

@socketio.on("disconnect")
def handle_disconnect():
    """
    Manejo de desconexión de un cliente.
    """
    print("Cliente desconectado.")

@socketio.on("command")
def handle_command(data):
    """
    Manejo de comandos enviados por el cliente.
    """
    print(f"Comando recibido: {data}")
    # Enviar una respuesta al cliente
    emit("server_response", {"message": f"Comando recibido: {data}"}, broadcast=True)

# Inicializar el servidor
if __name__ == "__main__":
    # Escuchar en el puerto 5000 o en el puerto proporcionado por la plataforma de despliegue
    socketio.run(app, host="0.0.0.0", port=5000)
