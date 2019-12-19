import datetime
import time

# check time difference

if __name__ == "__main__":
    before = datetime.datetime.now()  # get current time
    time.sleep(1)
    after = datetime.datetime.now()   # get next time
    print ("Elapsed Time = {0}".format(after - before))  # format time difference