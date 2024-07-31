numbers  = [5,2,5,2,2]

for number in numbers:
    print(f"x" * number)

for counter in numbers:
    output =""
    for x_count in range(counter):
        output += 'x'
    print(output)