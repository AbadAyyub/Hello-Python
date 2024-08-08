phone = input("Phone >")
mapper = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six"
}
output_string =""
for ch in phone:
   output_string += mapper.get(ch,"Not defined") + " "
print(output_string)
