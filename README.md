# Simulador de Máquina de Turing — Reconhecimento da Linguagem L = { aⁿbⁿ | n ≥ 0 }

Este repositório contém um simulador em Python de uma **Máquina de Turing Determinística (MTD)** projetada para reconhecer a linguagem formal:

L = { aⁿbⁿ | n ≥ 0 }

Essa linguagem compreende todas as cadeias compostas por uma sequência de `a`’s seguidos pela mesma quantidade de `b`’s, e é um exemplo clássico de linguagem não regular e não livre de contexto, que exige um modelo mais robusto como a Máquina de Turing para ser reconhecida.

---

## Sobre o projeto

A simulação reproduz fielmente o comportamento de uma MTD utilizando os seguintes elementos:

- **Fita**: representada por uma lista de caracteres.
- **Cabeçote de leitura/escrita**: controlado por um ponteiro de posição (índice).
- **Estados**: a máquina possui cinco estados principais (`q0`, `q1`, `q2`, `accept`, `reject`).
- **Função de transição**: implementada com estruturas condicionais em Python.

---

## Lógica da máquina

A MTD funciona por marcação:

1. Marca o primeiro `a` com `A`.
2. Busca o `b` correspondente e marca com `B`.
3. Retorna ao início da fita e repete o processo.
4. Se todos os símbolos forem pareados corretamente, a máquina aceita a palavra.

---

## Teste

O simulador foi testado com as seguintes entradas:

Palavras aceitas: "", ab, aabb, aaabbb

Palavras rejeitadas: aabbb, abb, aab
