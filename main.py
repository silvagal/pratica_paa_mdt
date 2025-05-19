def turing_machine_tape(word):
    # Adiciona espaço em branco no final da fita
    return list(word) + [' ']

def simulate_turing_machine(tape):
    state = 'q0'
    head = 0

    while True:
        symbol = tape[head]

        if state == 'q0':
            if symbol == 'a':
                tape[head] = 'A'
                head += 1
                state = 'q1'
            elif symbol in ['A', 'B']:
                head += 1
            elif symbol == ' ':
                state = 'accept'
            else:
                state = 'reject'

        elif state == 'q1':
            if symbol in ['a', 'A']:
                head += 1
            elif symbol == 'b':
                tape[head] = 'B'
                head -= 1
                state = 'q2'
            elif symbol == 'B':
                head += 1
            elif symbol == ' ':
                state = 'reject'
            else:
                state = 'reject'

        elif state == 'q2':
            if symbol in ['a', 'B', 'A']:
                head -= 1
            elif symbol == ' ':
                head += 1
                state = 'q0'
            else:
                state = 'reject'

        elif state == 'accept':
            return True
        
        elif state == 'reject':
            return False

# Testes
palavras = ["", "ab", "aabb", "aaabbb", "aabbb", "abb", "aab"]

for palavra in palavras:
    resultado = simulate_turing_machine(turing_machine_tape(palavra))
    if resultado:
        print(f"{palavra:8} → ACEITA")
    else:
        print(f"{palavra:8} → REJEITA")