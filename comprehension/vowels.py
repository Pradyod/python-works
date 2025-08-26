# words=['apple','bananna','orange','blueberry']

# vowels=[item for item in words if item[0] in ('a','e','i','o','u')]

# print(vowels)

sentence = "Hello, how are you today?"

vowels={i for i in sentence.lower() if i in ('a','e','o','u')}

print(vowels)