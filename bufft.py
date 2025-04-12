import os, sys
from time import sleep
from random import randint

VERSION = "0.1.0"


def bytec(bc):
    memory = {}
    ip = 0  # Instruction Pointer
    stack = []  # Стек для IFG
    while ip < len(bc):
        op = bc[ip]
        cmd = op[0]
        if cmd == "PUB":
            if op[1] == "INT": print(int(memory[op[2]]), end=" ")
            elif op[1] == "STR": print(str(memory[op[2]]), end=" ")
            elif op[1] == "VAL": print(" ".join(map(str, op[2:])), end=" ")
            elif op[1] == "NL": print()
        elif cmd == "INT": memory[op[1]] = int(op[2])
        elif cmd == "STR": memory[op[1]] = " ".join(op[2:])  # Добавляем пробелы между словами в строке
        elif cmd == "ARR": memory[op[1]] = list(map(int, op[2:]))
        elif cmd == "ADD":
            try: value = int(op[2])
            except ValueError: value = int(memory[op[2]])
            memory[op[1]] += value
        elif cmd == "SUB":
            try: value = int(op[2])
            except ValueError: value = int(memory[op[2]])
            memory[op[1]] -= value
        elif cmd == "MUL":
            try: value = int(op[2])
            except ValueError: value = int(memory[op[2]])
            memory[op[1]] *= value
        elif cmd == "DIV":
            try: value = int(op[2])
            except ValueError: value = int(memory[op[2]])
            memory[op[1]] /= value
        elif cmd == "REA":
            if op[1] == "INT": 
                try: 
                    memory[op[2]] = int(input()) 
                except: 
                    return 1
            elif op[1] == "STR": 
                try: 
                    memory[op[2]] = str(input()) 
                except:
                    return 1
        elif cmd == "MIF":  # Если var1 > var2
            if memory[op[1]] > memory[op[2]]:
                ip += 1  # Выполняем следующий код
                continue
            else:
                # Пропускаем до ELSE или END
                depth = 1
                while depth > 0 and ip < len(bc) - 1:
                    ip += 1
                    next_cmd = bc[ip][0]
                    if next_cmd == "MIF": depth += 1
                    elif next_cmd == "ELSE" and depth == 1: break
                    elif next_cmd == "END": depth -= 1
        elif cmd == "ELSE":
            # Пропускаем до END
            depth = 1
            while depth > 0 and ip < len(bc) - 1:
                ip += 1
                next_cmd = bc[ip][0]
                if next_cmd == "MIF":
                    depth += 1
                elif next_cmd == "END":
                    depth -= 1
            if stack: stack.pop()
        elif cmd == "END":
            if stack: stack.pop()

        ip += 1  # Увеличиваем ip по умолчанию после каждой команды


def parse_bufft_assembly(filename):
    bytecode = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line or line.startswith(';'):  # Пропускаем пустые строки и комментарии
            continue

        parts = line.split()
        if not parts:  # Пропускаем строки без содержимого
            continue

        cmd = parts[0].upper()  # Команда в верхнем регистре
        args = parts[1:]  # Все аргументы после команды

        # Формируем байт-код на основе структуры строки
        if len(args) == 0:
            # Команды без аргументов (например, ELSE, END)
            bytecode.append([cmd])
        elif len(args) == 1:
            # Команды с одним аргументом (например, PUB NL)
            bytecode.append([cmd, args[0].upper()])
        elif len(args) >= 2:
            # Команды с двумя и более аргументами
            if cmd == 'STR':
                # Для STR собираем все аргументы в строку и разбиваем на слова
                value = ' '.join(args[1:])
                bytecode.append([cmd, args[0]] + value.split())
            else:
                # Для всех остальных команд просто добавляем аргументы как есть
                bytecode.append([cmd, args[0]] + args[1:])

    return bytecode


# Проверка аргументов и запуск
if len(sys.argv) >= 2:
    filename = sys.argv[1]
    if filename == "V": 
        print(VERSION)
    else:
        try:
            bufft_bytecode = parse_bufft_assembly(filename)
            bytec(bufft_bytecode)
        except FileNotFoundError:
            print(f"Файл {filename} не найден")
        except Exception as e:
            print(f"Ошибка: {e}")
        print()  # Новая строка после выполнения
else:
    print("Укажите имя файла как аргумент")
    os.system("pause")
