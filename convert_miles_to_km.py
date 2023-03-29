# a program to convert km into miles 
# just a practice program
# this code block converts km into miles
def miles_into_km(km_input):
    #print(km_input)
    formula_mile = km_input*0.62137119
    return formula_mile

  # this block converts miles into km
def km_into_miles(miles_input):
    formula_km = miles_input*1.609344
    return formula_km
    if (km_input>miles_input):
      return km_input+ "is the greatest number"
    else:
      return miles_input+ "is the gteatest number "


      
km_input = float(input("enter the km value = "))
miles_input = float(input("enter the miles value = "))
a = miles_into_km(km_input)
b = km_into_miles(miles_input)
print("the km converted to miles value is = ",a)
print("the miles converted to km be = ",b)
print()