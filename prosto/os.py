import json
import os
import platform
import psutil


def main():
    data = search_data()
    save_data(data)


def search_data():
    cpu_count = psutil.cpu_count(logical=False)      # физические ядра
    logical_count = psutil.cpu_count(logical=True)   # логические процессоры

    cpu_usage = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()
    total_memory = memory.total
    used_memory = memory.used

    cpu_speed = psutil.cpu_freq()

    if cpu_speed:
        current_speed = cpu_speed.current
        max_speed = cpu_speed.max
    else:
        current_speed = None
        max_speed = None

    processes = len(psutil.pids())

    computer_name = platform.node()

    data = {
        "Имя компьютера": computer_name,
        "Физические процессоры": cpu_count,
        "Логические процессоры": logical_count,
        "Активные процессы": processes,
        "Загрузка процессора (%)": cpu_usage,

        "Оперативная память (ГБ)": round(total_memory / (1024 ** 3), 2),
        "Используется ОЗУ (ГБ)": round(used_memory / (1024 ** 3), 2),
        "Используется ОЗУ (%)": memory.percent,

        "Текущая скорость процессора (МГц)": current_speed,
        "Максимальная скорость процессора (МГц)": max_speed
    }

    return data


def save_data(data: dict):
    name = "data.json"

    with open(name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


main()