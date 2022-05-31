from flask import Flask, request, jsonify, render_template, redirect, url_for

from model import *

app = Flask(__name__)
app.secret_key = "c2K#&b6Dz0_6)Ck63z@IIrbp6e&T&*Q2AIlD@%7LmXXu9q+ya33%#W&X_PAxKR2pHnp"



@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'),500

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


@app.route("/classifier", methods=["POST", "GET"])
def classifier():
    return render_template('classifier-responsive.html')

@app.route("/analyze", methods = ['GET', 'POST'])
def perform_analysis():
    if request.method == 'POST':

        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files.get('file')
        if not file:
            return
        img_bytes = file.read()
        # client_shoe_image = diplay_image(img_bytes)
        model = get_model()
        class_names_and_values = get_top_5_predictions(img_bytes, model)
        class_names_and_values = [f'{index+1}. {value[0]} \t {value[1]*100:.2f}%' for index, value in enumerate(class_names_and_values)]


        return render_template('result-responsive.html', class_names_and_values=class_names_and_values)

    return redirect(url_for('classifier-responsive'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)


