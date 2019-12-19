import datetime
import time

def time_this(original_function,n):
    def new_function(*args, **kwargs):
        before = datetime.datetime.now()
        # x = original_function(*args, **kwargs)
        x = original_function(n)
        after = datetime.datetime.now()
        print ("Elapsed Time = {0}".format(after - before))
        return x
    return new_function()

# first way, we use the following @time_this for the decorator
@time_this
def func_a(n):
    print ("func_a before sleep")
    time.sleep(n)
    print ("func_a after sleep")

if __name__ == "__main__":

   # second way, we call the time_this directly to time func_a
   # this way works, but the code is ugly.
   # so we normally use the first way
   time_this(func_a,5)




'''
 reference:
 1. https://www.codementor.io/sheena/introduction-to-decorators-du107vo5c
 2. https://www.codementor.io/sheena/advanced-use-python-decorators-class-function-du107nxsv
 3. 

'''