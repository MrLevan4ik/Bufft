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
                try: memory[op[2]] = int(input())
                except: return 1
            elif op[1] == "STR":
                try: memory[op[2]] = str(input())
                except: return 1
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