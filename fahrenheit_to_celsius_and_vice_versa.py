print("___________________________________________________________________________________________________________________")
print("")
def calculate_celsius_to_fahrenheit(val):
    celsius_to_fahrenheit= (val*(9/5)+32)
    return celsius_to_fahrenheit

fahrenheit_value= float(input("enter the number to convert it from celsius to fahrenheit = "))
inval = calculate_celsius_to_fahrenheit(fahrenheit_value)
print(inval)


# now convert the given value from fahrenheit to celsius 
def convert_fahrenheit_to_celsius (val2):
    formual_for_converting_f_to_c = (val2 - 32)*5/9 
    return formual_for_converting_f_to_c 

input_val = float(input("enter the fahrenheit value = "))
final_val= convert_fahrenheit_to_celsius(input_val)
print(final_val)

print("the final values of f to c is {} and c to f is {}".format(inval,final_val))
print("__________________________________________________________________________________________________-")
