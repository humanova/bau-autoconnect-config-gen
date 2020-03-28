from flask import Flask, render_template, jsonify, request
import json

app = Flask("bau-autoconnect", template_folder="src/templates")

# config generator frontend
@app.route('/bau-autoconnect-config')
def config_page():
    return render_template('config.html')

# maybe a middleware to do stuff ?
# TODO: anonymously save configs
@app.route('/bau-generate-config', methods=['POST'])
def gen_config():
    config_dict = request.json['config_dict']
    return jsonify({"courses" : config_dict})

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)