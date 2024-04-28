import time
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

team = []
types = ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy", "Flying", "Electric", "Psychic", "Bug", "Rock", "Ice", "Fairy", "Dragon", "Steel", "Ghost"]

# select a random Pokemon type
def rtype(): return random.choice(types)

# select a random pokemon of given type
def rpokemon(type):
    path = f"Pokemon/{type}.txt"
    listmon = open(path, "r")
    pokemon = listmon.read().split(";")
    listmon.close()

    return random.choice(pokemon)

# due to dual type pokemon, we need to check if the pokemon is already in the list,
# if it is select another pokemon, else add it to the team and remove the type from the list.
def check(pokemon, ptype, i):
    if pokemon in team:
        rpokemon(ptype)
        check(pokemon)
    else:
        team.append(f"{i}. {pokemon}")
        types.remove(ptype)


def main():
    team_size = 6
    for i in range(team_size):
        ptype = rtype()
        pokemon = rpokemon(ptype)
        check(pokemon, ptype, i+1)

    for mon in team:
        logging.info(mon)

    while True:
        time.sleep(3600)  # Sleep for 1 hour


if __name__ == "__main__":
    main()
