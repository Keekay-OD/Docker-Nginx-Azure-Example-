from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Test Site Madce by Omar Diaz!'

if __name__ == '__main__':
  app.run()
