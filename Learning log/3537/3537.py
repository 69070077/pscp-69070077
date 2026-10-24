"""Imposter"""
import json
def main():
    """Imposter"""
    alive = {}
    dead = {}
    while True:
        text = input()
        if text == "Start":
            break
        player = json.loads(text)
        alive.update(player)
    while True:
        kick_player = input()
        if kick_player == "End":
            break
        if kick_player in alive:
            role = alive.pop(kick_player)
            dead[kick_player] = role

    impostor = list(alive.values()).count("Impostor")
    print(f"{impostor} Impostor Remains")

    print("***Alive***")
    for name in sorted(alive.keys()):
        print(f"{name} : {alive[name]}")

    print("***Dead***")
    for name in sorted(dead.keys()):
        print(f"{name} : {dead[name]}")
main()
