#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 

from subprocess import check_output

train_variant = pd.read_csv("../input/training_variants")
train_text = pd.read_csv("../input/training_text", sep="\|\|", engine='python', header=None, skiprows=1, names=["ID","Text"])

test_variant = pd.read_csv("../input/test_variants")
test_text = pd.read_csv("../input/test_text", sep="\|\|", engine='python', header=None, skiprows=1, names=["ID","Text"])

train = pd.merge(train_variant, train_text, how='left', on='ID')
x_train = train.drop('Class', axis=1)

testing_variants_df = pd.read_csv("../input/test_variants")
testing_text_df = pd.read_csv("../input/test_text", sep="\|\|", engine='python', header=None, skiprows=1, names=["ID","Text"])
testing_merge_df = testing_variants_df.merge(testing_text_df,left_on="ID",right_on="ID")
