import sys

def is_message_valid(filename):
    """
    This function searches a file for an email address or phone number using the helper methods defined above.
    If the file contains a phone number or email address, it is considered invalid and the function should
    return False. If it contains neither a phone number or email address, the message is valid and should
    return True.
    >>> is_message_valid('100284.txt')
    True
    >>> is_message_valid('100282.txt')
    True
    >>> is_message_valid('100280.txt')
    False
    """
    with open(filename, 'r') as f:
        for line in f:
            if check_email(line):
                return False
            if check_phone(line):
                return False
            return True

def check_phone(line):
    for i in range(len(line)):
        if line[i].isdigit():
            substring = line[i:i + 10]
            if substring.isdigit():
                return True
    return False

def check_email(line):
    location = line.find('@')
    if location == -1:
        return False
    if line[location - 1] == ' ' or line[location + 1] == ' ':
        return False
    return True

def main(args):
    try:
        filename = args[0]
        if is_message_valid(filename):
            print("Message is valid!")
        else:
            print("Message is not valid!")
    except Exception as e:
        print("Failed to check file... are you sure you inputted a valid filename?")

if __name__ == "__main__":
    main(sys.argv[1:])
