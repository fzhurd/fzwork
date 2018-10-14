# -*- coding: utf-8 -*-

import pickle

def serialized_model(model, serialized_model_file_name):
    pickle.dump(model, open(serialized_model_file_name, 'wb'))

def deserialized_model(serialized_model_file_name):
    loaded_model = pickle.load(open(serialized_model_file_name, 'rb'))
    return loaded_model
