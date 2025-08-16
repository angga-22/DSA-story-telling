


# primitive yee, 
# string, boolean, integer, double
# 
my_string = "test string"
my_bool = True # False
my_double = 5.5
my_int = 5

list_to_str = ' '.join(["angga", "saputra", "!"])
print(list_to_str)
str_to_list = "angga ganteng".split()
str_to_list_2 = list("angga ganteng sekali")
print(str_to_list)
print(str_to_list_2)

str_replace = "angga ganteng".replace("ganteng", "jelek")
print(str_replace)
str_alpha = "angga".isalpha()
str_alphanum = "angga123".isalnum()
str_int  = "123".isalnum()
# tuple

my_tuple = (1,2, 3, 4) 

# set, unique, any same el will auto removed
my_set = {1, 2, 3, 4}

# dictionary
data_diri = {
    "firstName": "angga",
    "lastName": "saputra",
    "age": 50,
    "isMarried": True
}


first_name = data_diri["firstName"]
data_diri["add_attr"] = "test add attr"
del data_diri["age"]
print(data_diri)



# list
my_list = [1, 2, 3, 4, 5, True, "tes"]

# slice broh
print(my_list[:2]) # [1, 2]
print(my_list[2:]) # [3, 4, 5, True, "tes"]
print(my_list[-1]) # tes 
print(my_list[3:5]) # [4, 5]
print(my_list[0::2]) # [1, 3, 5, 'tes']
print(my_list[::2]) # [1, 3, 5, 'tes']




# OPERATORS
# IN, NOT IN, COUNT, MIN, MAX
# consider understand!


# list destructure
my_list_desc = ['shirt', 'motor', 'house']
s, m, h = my_list_desc


# list sort
my_sorting = [5, 2, 1, 5, 6, 3]
my_sorting.sort(reverse=True) # sort the original
my_sorted = sorted(my_sorting, reverse=False)
print(my_sorted, 'why')
















