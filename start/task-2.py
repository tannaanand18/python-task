# My Second task 

emails = [
    "anand@gmail.com",
    "raj@yahoo.com",
    "manthan@gmail.com",
    "himanshu@outlook.com",
    "shubham@gmail.com"
]

counts = {}

for email in emails:
    pos = email.find("@")
    domain = email[pos+1:]

    if domain in counts:
        counts[domain] += 1

    else:
        counts[domain] = 1

for domain, count in counts.items():
    print(domain, ":", count)