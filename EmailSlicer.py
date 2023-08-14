import re
email = input("Enter your email address: ")
pattern = r"([\w]+)@([\w]+\.[\w]+)"
match = re.match(pattern, email)
username = match.group(1)
domain_name = match.group(2)
print("Username:", username)
print("Domain name:", domain_name)