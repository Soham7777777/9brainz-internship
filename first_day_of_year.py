from enum import StrEnum, auto


FIRST_DAY_OF_2025 = 2


class Day(StrEnum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THRUSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()


def solution(year: int) -> int:
    if year == 2025 : return FIRST_DAY_OF_2025

    if year > 2025:
        l, r = 2025, year
    else:
        l, r = year, 2025
    
    total_days = 0

    for y in range(l, r):
        if (y % 4) == 0 : total_days += 366
        else: total_days += 365
    
    result = total_days % 7 if l == 2025 else 7 - (total_days % 7)

    return (result + FIRST_DAY_OF_2025) % 7


def main() -> None:
    for i in range(2025, 2029 + 1):
        print([*Day][solution(i)])

    print()

    for i in range(2024, 2020 - 1, -1):
        print([*Day][solution(i)])


if __name__ == "__main__":
    main()
