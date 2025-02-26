 # datatypes.py
#Variables of each data type
int_var = 25
float_var = 9.5
complex_var = 5 + 4j
list_var = [1, 2, 3, 4, 5]
tuple_var = (6, 7, 8, 9, 10)
dict_var = {'country': 'Kenya', 'city': 'Nairobi'}
set_var = {11, 12, 13, 14, 15}
bool_var = False

# Printing the variable types
print("Type of int_var:", type(int_var))
print("Type of float_var:", type(float_var))
print("Type of complex_var:", type(complex_var))
print("Type of list_var:", type(list_var))
print("Type of tuple_var:", type(tuple_var))
print("Type of dict_var:", type(dict_var))
print("Type of set_var:", type(set_var))
print("Type of bool_var:", type(bool_var))

# Converting int to float and vice versa
int_to_float = float(int_var)
float_to_int = int(float_var)
print("Integer to float:", int_to_float)
print("Float to integer:", float_to_int)
