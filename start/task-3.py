#  Third Task 

emails = [
    "anand@gmail.com",
    "raj@yahoo.com",
    "manthan@gmail.com",
    "himanshu@outlook.com",
    "shubham@gmail.com"
]

groups = {}

for email in emails:
    pos = email.find("@")
    domain = email[pos +1:]

    if domain in groups:
        groups[domain].append(email)

    else:
        groups[domain] = [email]

        print(groups)