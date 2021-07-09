### Checking if string is a phone number

def isPhoneNumber(text):
    if len(text) != 12:   # Checking if number is 12 symbols long
        return False
    for i in range(0, 3):   # Checking if first 3 symbols are numbers
        if not text[i].isdecimal():
            return False
    if text[3] != '-':    # Checking if symbol 4 is a -
        return False
    for i in range(4, 7):   # Checking if symbols 5 - 7 are numbers
        if not text[i].isdecimal():
            return False
    if text[7] != '-':    # Checking if symbol 8 is a -
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

