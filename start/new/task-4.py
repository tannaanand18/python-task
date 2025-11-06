import os

print("Files are being created in:", os.getcwd())

with open("users.txt", "r") as file:
    emails = file.read().splitlines()

groups = {}

for email in emails:
    pos = email.find("@")
    domain = email[pos+1:]

    if domain in groups:
        groups[domain].append(email)
    else:
        groups[domain] = [email]

# ✅ Correct place for filename (inside the loop)
for domain, email_list in groups.items():
    filename = domain.split(".")[0] + ".txt"   # gmail → gmail.txt

    # ✅ This saves output one folder UP
    with open("../" + filename, "w") as f:
        for email in email_list:
            f.write(email + "\n")

print("✅ Files created successfully!")
