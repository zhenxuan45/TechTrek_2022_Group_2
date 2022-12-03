from flask import Flask

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    return {'hello': 'world'}


app.run()