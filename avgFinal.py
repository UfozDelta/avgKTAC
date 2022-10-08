ktacList = []

# we know that the list size will always be 4
for i in range(0, 4):
    print("Enter the percentge weight of index", i)
    percentWeightOfKtac = int(input())
    ktacList.append(percentWeightOfKtac)

# the elments in list ktac will be used as a final weight to your overall average mark
print("The weights of KTAC in your course are ", ktacList)