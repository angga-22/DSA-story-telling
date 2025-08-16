# use try except

try:
    print("block code that may be have exception")
except:
    print("block statement executed if exception happens")
else:
    print("block statement executed if no exception happens")
finally:
    print("block statement executed after all ")


# example

var_dict = {"average": "1.0"}

try:
    print(f"average is {var_dict['average']}")
except KeyError:
    print("key not found")
except TypeError:
    print("you cannot divide value with string data type")
else:
    print("block executed if no exception")
finally:
    print("finish all ")


# raise

my_var = -1
if my_var < 0:
    raise ValueError("negative int not allowed")
else:
    for i in range(my_var):
        print(i+1)
