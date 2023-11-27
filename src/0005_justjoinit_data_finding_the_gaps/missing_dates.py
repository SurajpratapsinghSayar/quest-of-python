import pathlib
import calendar
from pathlib import Path


def get_days_in_month(year: int, month: int) -> int:
    _, days_in_month = calendar.monthrange(year, month)
    return days_in_month


def find_missing_dates(input_directory: Path) -> str:
    missing = ""

    for year in input_directory.iterdir():
        for month in year.iterdir():
            total_days = get_days_in_month(int(year.name), int(month.name))
            days = [int(str(day)[24:-5]) for day in month.iterdir()]
            for i in range(1, total_days + 1):
                if i not in days:
                    if i // 10 == 0:
                        i = f"0{i}"
                    missing += f"{year.name}-{month.name}-{i}, "

    return missing
