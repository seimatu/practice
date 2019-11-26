#global local

message='gergva'

def print_message():
    #the variable 'message' is local to the function inself

    global message
    #now message has become global function

    message='hello! I am going to banglore'
    return message

print(print_message())
print(message)



message='gergva'

def print_message():
    #the variable 'message' is local to the function inself


    #now message has become global function

    message='hello! I am going to banglore'
    return message

print(print_message())
print(message)