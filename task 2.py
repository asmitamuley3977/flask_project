import requests

# API link
url = "https://jsonplaceholder.typicode.com/users"

try:
    # Get data from API
    response = requests.get(url)

    # Check for error
    response.raise_for_status()

    # Convert JSON data into Python data
    users = response.json()

    print("Data received successfully!\n")

    # Show all users
    print("All Users:")

    for user in users:
        print(user["name"], "-", user["email"])

    # Search users from London
    print("\nUsers from London:")

    for user in users:
        if user["address"]["city"] == "London":
            print(user["name"], "-", user["email"])

except:
    print("Something went wrong!")
