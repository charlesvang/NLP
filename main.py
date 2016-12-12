
from flask import Flask

app = Flask(__name__, static_url_path='')

"""
@app.route('/api/seq2seq', methods=['POST'])
def seq2seq():
    print(request.json)
    return jsonify({"dude":"hello"})
"""
@app.route('/')
def root():
	return app.send_static_file("index.html")
@app.route('/')
def main_form():
	return '<textarea rows = "10" cols = "50" name = "input"> </textarea>'
app.run()
