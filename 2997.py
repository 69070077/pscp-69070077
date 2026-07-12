"""Elo"""
def main():
    """Elo"""
    Ra = int(input())
    Rb = int(input())
    who = input()
    Ea = 1 / (1 + 10**((Rb - Ra )/ 400))
    Eb = 1 / (1 + 10**((Ra - Rb )/ 400))
    if who == 'A':
        print(f"{Ea:.2f}")
    elif who == 'B':
        print(f"{Eb:.2f}")
main()
