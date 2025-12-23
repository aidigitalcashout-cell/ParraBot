# app.py

from flask import Flask
from routes import admin_routes
import threading

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(admin_routes, url_prefix='/admin')

def start_server():
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    server_thread = threading.Thread(target=start_server)
    server_thread.start()
