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





# OUTPUT :
Data received successfully!

All Users:
Leanne Graham - Sincere@april.biz
Ervin Howell - Shanna@melissa.tv
Clementine Bauch - Nathan@yesenia.net
Patricia Lebsack - Julianne.OConner@kory.org
Chelsey Dietrich - Lucio_Hettinger@annie.ca
Mrs. Dennis Schulist - Karley_Dach@jasper.info
Kurtis Weissnat - Telly.Hoeger@billy.biz
Nicholas Runolfsdottir V - Sherwood@rosamond.me
Glenna Reichert - Chaim_McDermott@dana.io
Clementina DuBuque - Rey.Padberg@karina.biz

Users from London:

Process finished with exit code 0
