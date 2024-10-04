from flask import Flask
from threading import Thread
import backend_code
Thread(target=backend_code.run).start()

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Back4apper!"
    
def run():
    @client.request
    def ping(): #called when client receives request
        print("Ping request received")
        return "pong" #sends back 'pong' to the Scratch project
    
    @client.event
    def on_ready():
        print("Request handler is running")
    
    @client.request
    def foo(argument1):
        print(f"Data requested for user {argument1}")
        user = scratch3.get_user(argument1)
        stats = user.stats()
    
        return_data = []
        return_data.append(f"Total loves: {stats['loves']}")
        return_data.append(f"Total favorites: {stats['favorites']}")
        return_data.append(f"Total views: {stats['views']}")
    
        return return_data
    
    client.run() #make sure this is ALWAYS at the bottom of your Python file




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
