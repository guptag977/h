from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Home Page Route
@app.route('/')
def index():
    return render_template('index.html')

# Download Function
@app.route('/download/<filename>')
def download_file(filename):
    # 'static/files' folder se file ko download karne ke liye
    return send_from_directory('static/files', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)