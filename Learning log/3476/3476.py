"""CuteCatCuteFox"""
import ast
def main():
    """CuteCatCuteFox"""
    num = int(input())
    pet = {}

    for _ in range(num):
        d = ast.literal_eval(input())
        for k in d:
            pet[k] = d[k]

    code = set(pet.values())
    if "Cat01" not in code and "Garfield" not in pet:
        pet["Garfield"] = "Cat01"
    if "Fox01" not in code and "Fubuki" not in pet:
        pet["Fubuki"] = "Fox01"

    cat = [(v, k) for k, v in pet.items() if v.startswith("Cat")]
    fox = [(v, k) for k, v in pet.items() if v.startswith("Fox")]
    cat.sort(key=lambda t: int(t[0][3:]))
    fox.sort(key=lambda t: int(t[0][3:]))

    print(f"Cat : {len(cat)}")
    print(f"Fox : {len(fox)}")

    for v, k in cat:
        print(f"{k} : {v}")
    for v, k in fox:
        print(f"{k} : {v}")
main()
