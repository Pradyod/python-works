words=["word","madam","racecar","car"]

# for w in words:
#     if w==w[::-1]:
#         print(w,"is a pallindrome")

ke=[w for w in words if w==w[::-1]]
print(ke)