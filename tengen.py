import string, json

a = list(string.ascii_lowercase)+list(string.digits) # Creates a list of characters: a-z,0-9

b = [[i*3+'+'+j*3+'", "'+i+j+i+j] for i in a for j in a] # Iterates through the list creating question-answer pairs

b = json.dumps(b) # Removes single quotes
b = b.replace('\\','') # Removes the backslash added by json.dumps

print(b)
