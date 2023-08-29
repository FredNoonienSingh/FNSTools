from __future__ import annotations
import tracemalloc
from time import time
from datetime import datetime
from functools import wraps
from csv import writer
from typing import Any

class returnCatcher:
    """ 'catches the Return Value of a function within the wrapper, to store and return it 
    """
    def __init__(self, func) -> None:
        self.func = func
        self.val = None

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.val = self.func(*args, **kwargs)

def functionPerformance(func:callable)-> None:
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        st = time()
        tracemalloc.start()
        retVal = returnCatcher(func)
        retVal(*args, **kwargs)
        et = time()
        current, peak = tracemalloc.get_traced_memory()
        delta_time = et-st
        if kwargs.get("verbose", False):
            print("\n"*3,"__"*30)
            print(f"\nFUNCTION: {func.__name__.upper()}\n   ","=="*25,
                    f"\n\tExecutionTime\t\t {delta_time:.5f} seconds"
                    f"\n\tMemory usage:\t\t {current / 10**6:.6f} MB"
                    f"\n\tPeak memory usage:\t {peak / 10**6:.6f} MB")
            print("__"*30, "\n"*3) 
        tracemalloc.stop()
        return retVal.val
    return wrapper
