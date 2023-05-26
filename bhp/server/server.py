from flask import Flask, request, jsonify
import util

app = Flask(__name__)

#@app.route('/get_location_names', methods=['GET'])
@app.route('/get_locations', methods=['GET'])
def get_locations():
    response = jsonify({
        'locations': util.get_locations()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_house_price', methods=['GET', 'POST'])
def predict_house_price():
    total_sqft = float(request.form.get('total_sqft'))
    location = request.form.get('location')
    bhk = int(request.form.get('bhk'))
    bath = int(request.form.get('bath'))

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Predicting house prices...")
    #util.load_saved_artifacts()
    util.load_artifacts()
    app.run()