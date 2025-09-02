import requests

mydb = {
    1: ["Alice", "alice@abc.com"],
    2: ["Mary","mary@abc.com"],
    3: ["Christopher", "christopher@abc.com"]
}

def get_user_by_id(id):
    return mydb.get(id, [None])[0]

def get_email_by_id(id):
    return mydb.get(id, [None, None])[1]

def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return(response.json())

    raise requests.HTTPError


if __name__ == "__main__":
    get_users()