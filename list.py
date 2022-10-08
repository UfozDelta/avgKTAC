# F3L
# Knowledge Portion

# Knowledge Testing Material Portion 
knowledgeMark = []
knowledgeLength = int(input("Enter ammount of Knowledge tests "))

print("\n")
for i in range(0, knowledgeLength):
    print("Enter K mark", i, )
    item = int(input())
    knowledgeMark.append(item)
print("Knowledge Marks are ", knowledgeMark)

# Weighting for Each Knowledge
knolwedgeWeights = []

print("\n")
for i in range(0, knowledgeLength):
    print("Enter weight of Knowledge mark ", knowledgeMark[i])
    item = int(input())
    knolwedgeWeights.append(item)
print("The weight of kListWeight is ", knolwedgeWeights)

# Multiply each value by the weights of each data point of knowledge 
finalKnowledgeWeights = []

print("\n")
for i in range(0, knowledgeLength):
    final = knowledgeMark[i] * knolwedgeWeights[i]
    finalKnowledgeWeights.append(final)

# Final Weight
fKnowWeight = (sum(finalKnowledgeWeights)) / (sum(knolwedgeWeights))
print("Final Mark is", fKnowWeight)