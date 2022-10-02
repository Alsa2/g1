import hmac


def simple_login(username:str, password:str) -> bool:
    """This function receives a username and a password and returns True if the username is in the database and the password is correct, otherwise returns False"""

    with open("user.csv", "r") as file:
        database = file.readlines()
    salty = "(╯°□°）╯︵ ┻━┻"
    to_hash = username + password + salty
    hashed_password = hmac.new(''.encode(), to_hash.encode(),  'sha512').hexdigest()
    
    output = False
    for line in database:
       line_cleaned = line.strip()
       user, password = line_cleaned.split(",")
       if user == username and password == hashed_password:
           output = True
           break
    return output


