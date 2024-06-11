#!/bin/env python
from app import create_app, socketio

app = create_app(debug=True)
socketio_port = 5000

if __name__ == '__main__':
    # Use o host '0.0.0.0' e a porta definida para permitir conexões de qualquer endereço IP
    socketio.run(app, host='0.0.0.0', port=socketio_port)
