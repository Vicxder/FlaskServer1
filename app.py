from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('Mensaje recibido:', message)
    send('Comando recibido', broadcast=True)  # Envía una respuesta al cliente

if __name__ == '__main__':
    socketio.run(app)
