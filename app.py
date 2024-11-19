from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict()
    file = request.files.get('file')
    print(f"Form Data: {data}")
    if file:
        print(f"Uploaded File: {file.filename}")
    return jsonify({"message": "Form submitted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
