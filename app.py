import os
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'C:\\Users\\sthelluri1\\Desktop\\HackGT2022\\uploads'
@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/about.html', methods=['GET', 'POST'])
def hello_from_about():
	return render_template("about.html")

@app.route('/index.html')
def return_here():
	return render_template('index.html')

@app.route('/upload.html', methods=['GET', 'POST'])
def upload_da_file():
	return render_template('upload.html')

@app.route('/song.html', methods=['GET', 'POST'])
def song_page():
	if request.method == 'POST':
		info = request.form
		file = request.files['file']
		fin = file.filename
		res_p = os.path.join(app.config['UPLOAD_FOLDER'], (fin).replace("/", "\\"))
		file.save(res_p)
		print(res_p)
		print("\\"+file.filename)
		#ris_p = res_p.replace('\\', "\\\\")
		#print(ris_p)
	return render_template('song.html', tit=info['titleArea'], desc=info['descriptionArea'], fn=fin)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=5000)

