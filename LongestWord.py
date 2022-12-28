sentence=input("Enter The Sentence: ")
longest=max(sentence.split(),key=len)
print("Longest Word Is : ",longest)
print("And Its Length Is: ",len(longest))