#!/usr/bin/python
# -*- coding: utf-8 -*-



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
	pass


if __name__ == '__main__':
	main()