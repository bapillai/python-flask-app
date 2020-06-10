from flask import Flask
app = Flask(__name__)

#Basic Routing
@app.route("/")
def main():
    return "Welcome!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}".format(name)

#Check if the execute file is the main program and run the app.
if __name__ == "__main__":
    app.run()