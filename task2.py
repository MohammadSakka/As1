import time
import inspect
import io
import contextlib

def decorator_2(func):
    def wrapper(*args,**kwargs):
        wrapper.calls +=1
        t = time.time()
        # Perhaps, it's more reasonable to use contextlib here, to not duplicate code of function call.
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            result = func(*args, **kwargs)
        exec_time = time.time() - t
        print(func.__name__ + " call" ,wrapper.calls, " executed in ", exec_time, " sec") 
        print("Name: ",func.__name__)
        print("Type: ",type(func))
        print("Sign: " ,inspect.signature(func))
        print("Args: ", "positional ", args, "\n", "\tkey=worded ", kwargs)
        print("Doc: " ,func.__doc__)
        # You can align your source code while printing to make output more beautiful)
        # You can split getsource by '\n' and print each line with the same indentation.
        print("Source: " ,inspect.getsource(func))
        
        s = f.getvalue()
        print('Output:', end = "")
        for l in s.splitlines():
             print('\t'+l)
    
        # It's better to return result of the function, because otherwise you cannot get the result of the function.
        return result
        

    wrapper.calls = 0
    return wrapper

