
import time
import numpy as np

def timerDecorator(function):

    def wrapper(n):
        start = time.time()
        function(n)
        end = time.time()
        print("function took " + str(end-start) + " seconds to run")

    return wrapper

@timerDecorator
def printNpArrayOfSize(n):
    return print(np.arange(n))

printNpArrayOfSize(100000000)