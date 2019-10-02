from fry251 import play
from flask import Flask


app = Flask(__name__)
 
@app.route("/")
def playgame():
    print('Hello let\'s play!')
    play()

if __name__ == "__main__":
    playgame.run(host='localhost', port=8081, debug=True)
