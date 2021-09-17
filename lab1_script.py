import requests

# Question 2 % 3
print(requests.__version__)
# Step 5
googleHomePage = requests.get("http://www.google.com/")
#print(googleHomePage.status_code)
#print(googleHomePage.text)

# Step 10
raw_link = "https://raw.githubusercontent.com/ZjTan4/cmput404lab1/main/lab1_script.py"
myself = requests.get(raw_link)
print(myself.text)