from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas
socketio = SocketIO(app, cors_allowed_origins="*")

# Ruta para la página HTML (opcional, si sirves el HTML desde Flask)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar comandos enviados vía HTTP (fallback)
@app.route('/control', methods=['POST'])
def control():
    data = request.get_json()
    if not data or 'command' not in data:
        return jsonify({'error': 'Comando inválido'}), 400

    command = data['command']
    print(f"Comando recibido vía HTTP: {command}")
    return jsonify({'message': f"Comando {command} recibido correctamente"}), 200

# WebSocket para manejar comandos en tiempo real
@socketio.on('message')
def handle_message(data):
    print(f"Mensaje recibido vía WebSocket: {data}")
    emit('response', {'message': f"Comando {data['command']} recibido correctamente"}, broadcast=True)

# Ruta para un feed de video simulado
@app.route('/video_feed')
def video_feed():
    # Simula una URL de feed de video; reemplaza con tu fuente real
    return jsonify({'message': 'Simulación de transmisión de video activa'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
