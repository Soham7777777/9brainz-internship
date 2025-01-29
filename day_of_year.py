from enum import StrEnum, auto
from typing import Literal, cast


DayNumberType = Literal[0, 1, 2, 3, 4, 5, 6]
MonthNumberType = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
DateNumberType = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]


class Day(StrEnum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THRUSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()


class Year:

    def __init__(self) -> None:
        self.numberOfDaysInEachMonthOfYear2024 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.firstDayOfYear2024 = Day.WEDNESDAY


    def getDayAtDate(self, date: DateNumberType, month: MonthNumberType) -> Day:
        daysPassed = self._getNumberOfDaysPassed(date, month) - 1
        dayNumber = daysPassed % 7
        dayNumber = (dayNumber + self._getDayNumberFromDay(self.firstDayOfYear2024)) % 7
        dayNumber = cast(DayNumberType, dayNumber)
        return Year._getDayFromDayNumber(dayNumber)


    def _getNumberOfDaysPassed(self, date: int, month: int) -> int:
        return sum(self.numberOfDaysInEachMonthOfYear2024[ : month]) + date


    @staticmethod
    def _getDayNumberFromDay(day: Day) -> DayNumberType:
        match day:
            case Day.MONDAY:
                return 0
            case Day.TUESDAY:
                return 1
            case Day.WEDNESDAY:
                return 2
            case Day.THRUSDAY:
                return 3
            case Day.FRIDAY:
                return 4
            case Day.SATURDAY:
                return 5
            case Day.SUNDAY:
                return 6        


    @staticmethod
    def _getDayFromDayNumber(dayNumber: DayNumberType) -> Day:
        match dayNumber:
            case 0:
                return Day.MONDAY
            case 1:
                return Day.TUESDAY
            case 2:
                return Day.WEDNESDAY
            case 3:
                return Day.THRUSDAY
            case 4:
                return Day.FRIDAY
            case 5:
                return Day.SATURDAY
            case 6:
                return Day.SUNDAY


def main() -> None:
    print(Year().getDayAtDate(1, 1))
    print(Year().getDayAtDate(2, 1))
    print(Year().getDayAtDate(3, 1))
    print(Year().getDayAtDate(4, 1))
    print(Year().getDayAtDate(5, 1))
    print(Year().getDayAtDate(6, 1))
    print(Year().getDayAtDate(7, 1))

    print()

    print(Year().getDayAtDate(17, 8))
    print(Year().getDayAtDate(31, 12))


if __name__ == "__main__":
    main()
