from flask import Flask, config, send_file
from modules import factory
import os

config_name = os.environ.get("CONFIG_NAME", "local")


app = factory.create_app(app_name="hungry-girlfriend", config_name=config_name)

@app.route('/')
def hello_world():
    send_file('index.html')

if __name__ == '__main__':
    app.run(port=8000)
