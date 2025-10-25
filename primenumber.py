primeNumbers=[]

for number in range(2, 251):
    if number > 1: 
        for i in range(2, number):
            if number % i== 0:
                break
        else:
            primeNumbers.append(number)
print("The list of the prime numbers 1-250 is:")
print(primeNumbers)

with open("results.txt", "w") as file:
    for p in primeNumbers:
        file.write(str(p)+",")
        