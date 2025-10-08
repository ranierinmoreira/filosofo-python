from flask import Flask, request

app = Flask(__name__, static_folder="static")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        email = request.form.get('email')
        senha = request.form.get('password')
        print(email, senha)
        return "OK POST"
    return "OK GET"

if __name__ == "__main__":
    app.run(debug=True)