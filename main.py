from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# 홈화면
@app.route('/')
def home_page():
	return render_template('home.html')

# 서버 실행
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug = True)