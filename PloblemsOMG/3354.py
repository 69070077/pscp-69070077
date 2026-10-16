"""Hint"""
import operator
def main():
    """Hint"""
    ops = {
    "==": operator.eq,
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "!=": operator.ne,
    }

    sym_nuy, val_nuy = input().split()
    val_nuy = int(val_nuy)
    sym_sib, val_sib = input().split()
    val_sib = int(val_sib)
    sym_roy, val_roy = input().split()
    val_roy = int(val_roy)

    for num in range(1000):
        roy = num // 100
        sib = (num // 10) % 10
        nuy = num % 10

        if (
            ops[sym_nuy](nuy, val_nuy)
            and ops[sym_sib](sib, val_sib)
            and ops[sym_roy](roy, val_roy)
        ):
            print(f"{num:03d}")
main()
