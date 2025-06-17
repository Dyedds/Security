import base64

user = "admin"
password = "nimda"

user_encoded = user.encode()
for _ in range(20):
    user_encoded = base64.b64encode(user_encoded)
user_str = user_encoded.decode()

password_encoded = password.encode()
for _ in range(20):
    password_encoded = base64.b64encode(password_encoded)
password_str = password_encoded.decode()

user_str = user_str.replace('1', '!').replace('2', '@').replace('3', '$') \
                   .replace('4', '^').replace('5', '&').replace('6', '*') \
                   .replace('7', '(').replace('8', ')')

password_str = password_str.replace('1', '!').replace('2', '@').replace('3', '$') \
                           .replace('4', '^').replace('5', '&').replace('6', '*') \
                           .replace('7', '(').replace('8', ')')

print("user=" + user_str)
print("")
print("password=" + password_str)
