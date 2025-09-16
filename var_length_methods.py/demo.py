# *args receive parameters as tuple
# **kwargs receive parameters as dict

def displya_person_details(*args):

    print(args)
    name=args[0]
    address=args[1]

    print(name)
    print(address)
    native_place=args


displya_person_details("james","street1","uk","london",45654)

def display_std_details(**kwargs):

    print(kwargs)

display_std_details(roll=1234,name="ron")
                       