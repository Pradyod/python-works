# words=['fish','tiger','giraffe','elephant','fox']

# w_dict={w:len(w) for w in words}

# print(w_dict)


# num=[2,4,6,8]

# sq_dict={i:i**2 for i in num}

# print(sq_dict)

order=['tea','tea','coffee','dosa','idly','biriyani','tea']

order_count={item:order.count(item) for item in order}

print(order_count)