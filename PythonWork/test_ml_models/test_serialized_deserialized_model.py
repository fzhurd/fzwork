# -*- coding: utf-8 -*-
import sys
print (sys.path)
sys.path.append("C:\\Users\\Frank2\\git\\fzwork\\PythonWork\\test_ml_models")

import unittest
import rf_model as rm
import knn_model as km
import lr_model as lm
import svm_model as sm
import serialized_deserialized_model as sdm



class SerializedDeserializedModelTest(unittest.TestCase):
    
    def setUP(self):
        pass
    
    def est_rf_model(self):
        self.new_rf_model = rm.build_rf_model()
        sdm.serialized_model(self.new_rf_model, 'rf_model2.bin')

        loaded_rf_model = sdm.deserialized_model('rf_model2.bin')
        result = loaded_rf_model.predict([[ 5]])
        print(result)
        self.assertEqual(1, result)
    
    def test_knn_model(self):
        self.new_knn_model = km.build_knn_model()
        sdm.serialized_model(self.new_knn_model, 'knn_model2.bin')

        loaded_knn_model = sdm.deserialized_model('knn_model2.bin')
        result = loaded_knn_model.predict([[ 20]])
        print(result)
        self.assertEqual(1, result)
    
    def test_lr_model(self):
        self.new_lr_model = lm.build_lr_model()
        sdm.serialized_model(self.new_lr_model, 'lr_model2.bin')

        loaded_lr_model = sdm.deserialized_model('lr_model2.bin')
        result = loaded_lr_model.predict([[ 20]])
        print(result)
        self.assertEqual(1, result)
    
    def test_svm_model(self):
        
        self.new_svm_model = sm.build_svm_model()
        sdm.serialized_model(self.new_svm_model, 'svm_model2.bin')

        loaded_svm_model = sdm.deserialized_model('svm_model2.bin')
        result = loaded_svm_model.predict([[ 20]])
        print(result)
        self.assertEqual(1, result)
    

if __name__=='__main__':
    unittest.main()

