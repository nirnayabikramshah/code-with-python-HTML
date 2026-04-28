import requests
base_url = 'https://pokeapi.co/api/v2'

def get_info(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url)
    pokemon_data= response.json()
    return pokemon_data


    if response.status_code ==200:
        print("connect successfully")
    else:
        print("Failed to connect")

pokemon_name =input("Enter the name of the pokemon :")
pokemon_info = get_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name']}")
    print(f"Id: {pokemon_info['id']}")
    print(f"Weight: {pokemon_info['weight']}Kg")
    print(f"Height: {pokemon_info['height']}Ft")


