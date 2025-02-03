import requests

from pydantic import BaseModel

class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        from_attributes = True

def pegar_pokemon(id: int) -> PokemonSchema:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()
    data_types = data['types']  # Supondo que 'data' é o dicionário com os dados do Pokémon
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    return PokemonSchema(name=data['name'], type=types)


if __name__ == "__main__":
    pokemon = pegar_pokemon(25)
    print(pokemon)