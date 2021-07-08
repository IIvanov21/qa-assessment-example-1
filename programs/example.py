    # <QUESTION 1>

    # Given a string, return the boolean True if it ends in "py", and False if not. Ignore Case.

    # <EXAMPLES>

    # endsPy("ilovepy") → True
    # endsPy("welovepy") → True
    # endsPy("welovepyforreal") → False
    # endsPy("pyiscool") → False

    # <HINT>

    # What was the name of the function we have seen which changes the case of a string?  Use your CLI to access the Python documentation and get help(str).
    
def endsPy(input):
    if input.endswith("py") or input.endswith("pY") or input.endswith("Py") or input.endswith("PY"):
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(endsPy("ilovepy") )
    print(endsPy("welovepY") )
    print(endsPy("welovepyforreal") )
    print(endsPy("pyiscool") )
