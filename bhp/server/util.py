import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    y = np.zeros(len(__data_columns))
    y[0] = sqft
    y[1] = bath
    y[2] = bhk
    if loc_index>=0:
        y[loc_index] = 1
    return np.round(float(__model.predict([y])), 2)

def load_artifacts():
    print("loading saved artifacts...")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # because first 3 columns are sqft, bath and bhk

    global __model
    if __model is None:
        with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("saved artifacts are loaded!!")

def get_locations():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_artifacts()
    print(get_locations())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('arekere', 1000, 2, 2))
    print(get_estimated_price('attebele', 1000, 2, 2))