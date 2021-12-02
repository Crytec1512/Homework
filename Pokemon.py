import requests


class BasePokemon:
    def __init__(self, name: str):
        self.name = name

    def printer(self):
        print(self.name, self.id, self.height, self.weight)


class Pokemon(BasePokemon):
    def __init__(self, id, name: str, height: int, weight: int) -> None:
            self.name = name
            self.id = id
            self.height = height
            self.weight = weight


class PokeAPI:

    def __init__(self):
        pass

    def get_pokemon(self) -> Pokemon:
        return Pokemon(requests.get(f'https://pokeapi.co/api/v2/pokemon/{self}').json()["id"],
                       requests.get(f'https://pokeapi.co/api/v2/pokemon/{self}').json()["name"],
                       requests.get(f'https://pokeapi.co/api/v2/pokemon/{self}').json()["height"],
                       requests.get(f'https://pokeapi.co/api/v2/pokemon/{self}').json()["weight"])

    def get_all(self, get_full= True) -> (BasePokemon, Pokemon):

        if isinstance(self, str):
            self = (requests.get(f'https://pokeapi.co/api/v2/pokemon/{self}').json()["id"])
        if get_full == False:
            while self != 0:
                yield BasePokemon(requests.get(f'https://pokeapi.co/api/v2/pokemon/{self}').json()["name"])
                self -= 1
        else:
            while self != 0:
                Poke = self.get_pokemon()
                yield Poke
                self -= 1


    EnterData = "ditto"
    PokeID = get_pokemon(EnterData)
    weight = 0

    for i in get_all(EnterData):
        if isinstance(i, Pokemon):
            if i.weight > weight:
                weight = i.weight

        elif isinstance(i, BasePokemon):
            print(i.name)
    print(weight)
    print(PokeID.id, PokeID.name, PokeID.height, PokeID.weight)





