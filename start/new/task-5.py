import os

print("Files will be created in:", os.getcwd())

groups = {}   # to store grouped records

with open("users.csv", "r") as file:
    lines = file.read().splitlines()

# Skip header (name,email)
for i in range(1, len(lines)):
    line = lines[i]
    name, email = line.split(",")     # Split into name and email

    pos = email.find("@")
    domain = email[pos+1:]            # extract domain (gmail.com etc.)

    if domain in groups:
        groups[domain].append((name, email))   # add tuple
    else:
        groups[domain] = [(name, email)]       # create list for new domain

# Now write separate CSV files
for domain, records in groups.items():
    filename = domain.split(".")[0] + "_users.csv"   # gmail → gmail_users.csv
    
    with open(filename, "w") as f:
        f.write("name,email\n")   # write header
        for name, email in records:
            f.write(name + "," + email + "\n")

print("✅ CSV files created successfully!")
