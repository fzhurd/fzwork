#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt


def monitor_time(func):

    @wraps(func)
    def calculate_time(*args, **kwargs ):
        start_time = time.time()
        result=func(*args, **kwargs)
        end_time=time.time()
        cost_time=end_time-start_time
        print(cost_time)
        return result

    return calculate_time





def main():

    titanic_df = pd.read_csv("../input/train.csv", dtype={"Age": np.float64}, )
    test_df    = pd.read_csv("../input/test.csv", dtype={"Age": np.float64}, )

    # preview the data
    print titanic_df.head(10)


if __name__ == '__main__':
	main()