a = "anand@gmail.com"

task = a.find("@")
domain = a[task+1:]

print(domain)