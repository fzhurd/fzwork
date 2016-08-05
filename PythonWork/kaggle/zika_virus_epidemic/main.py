#!/usr/bin/python
# -*- coding: utf-8 -*-

def import_data(data_file, mode):
    with open(data_file, mode) as f:
        lines = f.readlines()
        n=0
        for l in lines:
            n=n+1
            if n<10:
                print l

    

def main():
    import_data('cdc_zika.csv', 'r')


















if __name__ == '__main__':
    main()














