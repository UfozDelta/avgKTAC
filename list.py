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
knowledgeWeights = []

print("\n")
for i in range(0, knowledgeLength):
    print("Enter weight of Knowledge mark ", knowledgeMark[i])
    item = int(input())
    knowledgeWeights.append(item)
print("The weight of kListWeight is ", knowledgeWeights)

# Multiply each value by the weights of each data point of knowledge 
finalKnowledgeWeights = []

print("\n")
for i in range(0, knowledgeLength):
    final = knowledgeMark[i] * knowledgeWeights[i]
    finalKnowledgeWeights.append(final)

# Final Weight
fKnowWeight = (sum(finalKnowledgeWeights)) / (sum(knowledgeWeights))
print("Final Mark is", fKnowWeight)

# _________________________________________________
# Thinking Portion We repeat same steps but for thinking instead.
thinkingMark = []
thinkingLength = int(input("Enter Ammount of Knowledge Tests"))

print("\n")
for i in range(0, thinkingLength):
    print("Enter T Mark,", i)
    item = int(input())
    thinkingMark.append(item)
print("Thinking Marks are", thinkingMark)

# Weights for each thinking
thinkingWeights = []

print("\n")
for i in range(0, thinkingLength):
    print("Enter weight of Thinking mark ", thinkingMark[i])
    item = int(input())
    thinkingWeights.append(item)
print("The weight of Thinking weights is", thinkingWeights)

# Multiply each value by the weights of each dat point of thinking
finalThinkingWeights = []

print("\n")
for i in range(0, thinkingLength):
    final = thinkingMark[i] * thinkingWeights[i]
    finalThinkingWeights.append(final)

# Final Weight
fThinkWeight = (sum(finalThinkingWeights)) / (sum(thinkingWeights))
print("Final Mark is", fThinkWeight)


# __________________________________________________________
# Apply for Application
ApplicationMark = []
ApplicationLength = int(input("Enter Ammount of Knowledge Tests"))

print("\n")
for i in range(0, ApplicationLength):
    print("Enter T Mark,", i)
    item = int(input())
    ApplicationMark.append(item)
print("Application Marks are", ApplicationMark)

# Weights for each Application
ApplicationWeights = []

print("\n")
for i in range(0, ApplicationLength):
    print("Enter weight of Application mark ", ApplicationMark[i])
    item = int(input())
    ApplicationWeights.append(item)
print("The weight of Application weights is", ApplicationWeights)

# Multiply each value by the weights of each dat point of Application
finalApplicationWeights = []

print("\n")
for i in range(0, ApplicationLength):
    final = ApplicationMark[i] * ApplicationWeights[i]
    finalApplicationWeights.append(final)

# Final Weight
fThinkWeight = (sum(finalApplicationWeights)) / (sum(ApplicationWeights))
print("Final Mark is", fThinkWeight)



# __________________________________________________________
# Apply for Communication
CommunicationMark = []
CommunicationLength = int(input("Enter Ammount of Knowledge Tests"))

print("\n")
for i in range(0, CommunicationLength):
    print("Enter T Mark,", i)
    item = int(input())
    CommunicationMark.append(item)
print("Communication Marks are", CommunicationMark)

# Weights for each Communication
CommunicationWeights = []

print("\n")
for i in range(0, CommunicationLength):
    print("Enter weight of Communication mark ", CommunicationMark[i])
    item = int(input())
    CommunicationWeights.append(item)
print("The weight of Communication weights is", CommunicationWeights)

# Multiply each value by the weights of each dat point of Communication
finalCommunicationWeights = []

print("\n")
for i in range(0, CommunicationLength):
    final = CommunicationMark[i] * CommunicationWeights[i]
    finalCommunicationWeights.append(final)

# Final Weight
fThinkWeight = (sum(finalCommunicationWeights)) / (sum(CommunicationWeights))
print("Final Mark is", fThinkWeight)