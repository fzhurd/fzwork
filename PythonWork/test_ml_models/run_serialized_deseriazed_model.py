# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 23:41:23 2018

@author: Frank2
"""

import serialized_deserialized_model as sdm
import rf_model

rf_model = rf_model.build_rf_model()
sdm.serialized_model(rf_model, 'rf_model2.bin')

loaded_rf_model = sdm.deserialized_model('rf_model2.bin')
result = loaded_rf_model.predict([[ 1]])
print(result)