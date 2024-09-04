"""
Dada uma lista de palavras, use uma função lambda em conjunto com filter() para criar uma nova
lista contendo apenas as palavras que têm mais de 5 caracteres.

Instruções:

    Crie uma lista de strings, onde cada string representa uma palavra.

    Use a função filter() em conjunto com uma função lambda para filtrar as palavras que têm mais
    de 5 caracteres.

    Converta o resultado de filter() em uma lista e imprima a nova lista.

palavras = ["Python", "exercício", "lambda", "fácil", "filtrar", "palavras"]
"""

palavras = ["Python", "exercício", "lambda", "fácil", "filtrar", "palavras"]

palavras_filtradas = list(filter(lambda palavras: len(palavras) > 5, palavras))

print(palavras_filtradas)
