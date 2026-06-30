class MakepasswordError(Exception):
    pass
try:
    a=input()
    if len(a)<8:
        raise MakepasswordError("Error! Password must be 8 character")
    else:
        print("password accepted")
except MakepasswordError as e:
    print(e)
