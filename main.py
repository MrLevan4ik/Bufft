import os, sys, bytec, settings

def parse_bufft_assembly(filename):
    bytecode = []
    with open(filename, 'r', encoding='utf-8') as f: lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line or line.startswith(';'): continue
        parts = line.split()
        if not parts: continue

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
    if filename == "data": print(f"""
Bufft {settings.VERSION}
Developed by MrLevan4ik & BTXD
""")
    else:
        try:
            bufft_bytecode = parse_bufft_assembly(filename)
            bytec.bytec(bufft_bytecode)
        except FileNotFoundError:
            print(f"Файл {filename} не найден")
        except Exception as e:
            print(f"Ошибка: {e}")
        print()  # Новая строка после выполнения
else:
    print("Укажите имя файла как аргумент")
    os.system("pause")