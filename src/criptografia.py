import time

def cifraCesar(texto, chave):
    inicio = time.time()
    resultado = ""

    # Itera por cada caractere na string
    for caractere in texto:
        # Verifica se o caractere é uma letra maiúscula
        if caractere.isupper():
            # Encontra a posicao do caractere no alfabeto (A = 0, B = 1, ..., Z = 25)
            indice = ord(caractere) - ord('A')
            # Aplica a cifra de César
            novo_indice = (indice + chave) % 26
            # Converte o índice de volta para um caractere
            novo_caractere = chr(novo_indice + ord('A'))
            resultado += novo_caractere
        # Verifica se o caractere é uma letra minúscula
        elif caractere.islower():
            indice = ord(caractere) - ord('a')
            novo_indice = (indice + chave) % 26
            novo_caractere = chr(novo_indice + ord('a'))
            resultado += novo_caractere
        else:
            # Mantém o caractere inalterado (ex.: espacos, pontuacao)
            resultado += caractere
    fim = time.time()
    print(f"Tempo de execucao cifrar cesar: {fim-inicio:.2f} segundos")
    return resultado

def cifraAF(texto, chave):
    inicio = time.time()
    resultado = ""
    chave_str = str(chave)  # Converte a chave para string para iterar sobre os dígitos
    tamanho_chave = len(chave_str)

    for i, caractere in enumerate(texto):
        valor_ascii = ord(caractere)
        # Verifica se o caractere é imprimível
        if 32 <= valor_ascii <= 126:
            # Calcula o deslocamento com base no dígito correspondente da chave
            deslocamento = int(chave_str[i % tamanho_chave])
            # Aplica o deslocamento e utiliza a aritmética modular para manter no intervalo de 32 a 126
            novo_valor_ascii = 32 + ((valor_ascii - 32 + deslocamento) % 95)
            novo_caractere = chr(novo_valor_ascii)
        else:
            # Mantém o caractere inalterado se nao for imprimível
            novo_caractere = caractere

        resultado += novo_caractere
    fim = time.time()
    print(f"Tempo de execucao cifrar cifraAF: {fim-inicio:.2f} segundos")

    return resultado

def cifraAF2(texto, chave):
    inicio = time.time()
    resultado = ""
    chave_str = str(chave)  # Converte a chave para string para iterar sobre os dígitos
    tamanho_chave = len(chave_str)
    intervalo_inferior = 32
    intervalo_superior = 126
    intervalo_tamanho = intervalo_superior - intervalo_inferior + 1

    for i, caractere in enumerate(texto):
        valor_ascii = ord(caractere)
        
        if tamanho_chave > 1:
            # Calcula os índices para dois caracteres da chave
            indice_chave1 = (i * 2) % tamanho_chave
            indice_chave2 = (i * 2 + 1) % tamanho_chave
            
            if indice_chave2 < tamanho_chave:
                # Quando a chave é de tamanho ímpar e o segundo índice está fora dos limites, usa apenas o primeiro índice
                deslocamento = int(chave_str[indice_chave1] + chave_str[indice_chave2])
            else:
                deslocamento = int(chave_str[indice_chave1])  # Usa o último dígito sozinho
        else:
            deslocamento = int(chave_str)  # Caso a chave tenha apenas um dígito

        if intervalo_inferior <= valor_ascii <= intervalo_superior:
            novo_valor_ascii = intervalo_inferior + ((valor_ascii - intervalo_inferior + deslocamento) % intervalo_tamanho)
            novo_caractere = chr(novo_valor_ascii)
        else:
            novo_caractere = caractere

        resultado += novo_caractere
    fim = time.time()
    print(f"Tempo de execucao cifrar cifraAF2: {fim-inicio:.2f} segundos")
    return resultado
