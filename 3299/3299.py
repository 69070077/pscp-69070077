"""Flowerpot"""
import math as m
def main():
    """Flowerpot"""
    thick, tar = map(int, input().split())
    count = 1
    floor = 0
    multi = 1

    while count <= tar:
        count += multi
        multi += 1
        floor += 1
    print(m.ceil(floor / thick))

main()
