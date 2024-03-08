from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

# Sample list of movies
movies = [
    'BeeKeeper.mp4',
    'Dune(2021).mp4'
]

@app.route('/')
def index():
    client_hostname = request.remote_addr
    return render_template('index.html', movies=movies, client_hostname=client_hostname)

@app.route('/movies/<path:filename>')
def stream_movie(filename):
    return send_from_directory('movies', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
