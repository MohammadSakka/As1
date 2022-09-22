import time
import inspect
import io
import contextlib


fun_list = []
class decorator:
    def __init__(self,func):
        self.func = func
        decorator.count = 0
    def __call__(self,*args,**kwargs):
        decorator.count += 1
        self.arguments = args
        t = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as output:
            self.func(*args, **kwargs)
        exec_time = time.time() - t
        global fun_list
        with open('out.txt', 'a') as writer: 
            writer.writelines(self.func.__name__ + " call" + str(decorator.count)+ " executed in "+ str(exec_time)+ " sec\n") 
            writer.writelines(f"Name: {self.func.__name__}\n")
            writer.writelines(f"Type: {type(self.func)}\n")
            writer.writelines(f"Sign: {inspect.signature(self.func)}\n")
            writer.writelines(f"Doc:  {self.func.__doc__}\n")
            writer.writelines(f"Source:  {inspect.getsource(self.func)}\n")
            writer.writelines(f"Output:{output.getvalue()}\n")
        fun_list.append((self.func.__name__, exec_time))
        return self.func
    
def show():
    global fun_list
    fun_list.sort(key=lambda x: x[1])
    print("   name   rank    time")
    count = 1
    for f in fun_list:
        print(f[0],"   ",count,"   ",f[1],"\n")
    
    
