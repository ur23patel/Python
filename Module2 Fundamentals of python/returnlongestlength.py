Words = [ "one", "two", "three", "twelve", "fourteen"] 
Maxlen =0 
Longestword = " " 
for word in Words: 
	if len(word) > Maxlen: 
		Maxlen =len(word) 
		Longestword = word 
print(word, Maxlen) 
