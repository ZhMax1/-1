from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/img'


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return render_template('uploaded.html', filename=filename)


if __name__ == '__main__':
    app.run(debug=True)
