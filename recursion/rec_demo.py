"""
function call itself is called rescurion

def fucntion_name(parameter)
    base condition

    function_name(parameter)
"""

def count(n):

    if n==0:
        return
    print(n)

    return count(n-1)

count(5)    