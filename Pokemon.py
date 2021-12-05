import requests
from dataclasses import dataclass


@dataclass(frozen=True)
class BasePokemon:
    name: str


@dataclass(frozen=True)
class Pokemon(BasePokemon):
    name: str
    id: int
    height: int
    weight: int
#Здесь должен был быть __new__()


class PokeAPI:
    def __init__(self):
        pass

    def get_pokemon(self: (int, str)) -> Pokemon:
        return Pokemon(requests.get(f'https://pokeapi.co/api/v2/pokemon/{self}').json()["name"],
                       requests.get(f'https://pokeapi.co/api/v2/pokemon/{self}').json()["id"],
                       requests.get(f'https://pokeapi.co/api/v2/pokemon/{self}').json()["height"],
                       requests.get(f'https://pokeapi.co/api/v2/pokemon/{self}').json()["weight"])

    def get_all(self: int, get_full=True) -> (BasePokemon, Pokemon):    #Параметр get_full
        if not get_full:
            for i in range(898):    #Всего в API 898 покемонов
                if i + 1 <= self:
                    yield BasePokemon(requests.get(f'https://pokeapi.co/api/v2/pokemon/{i + 1}').json()["name"])

        else:
            for i in range(898):
                if i + 1 <= self:
                    yield i+1

    EnterData = "ditto"     #Покемон на вывод
    How_Many = 50           #Сколько первых покемонов
    PokeID = get_pokemon(EnterData)
    weight = 0
    print(PokeID.name, PokeID.id, PokeID.height, PokeID.weight)
    for object in get_all(How_Many):
        if isinstance(object, int):
            Poke = get_pokemon(object)
            print(Poke)
            if Poke.weight > weight:
                weight = Poke.weight

        elif isinstance(object, BasePokemon):
            print(object.name)

    print(weight)

