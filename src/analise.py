import time

def DescriptografacifraCesar(texto, chave):
    inicio = time.time()
    resultado = ""

    # Itera por cada caractere na string
    for caractere in texto:
        # Verifica se o caractere é uma letra maiúscula
        if caractere.isupper():
            # Encontra a posicao do caractere no alfabeto (A = 0, B = 1, ..., Z = 25)
            indice = ord(caractere) - ord('A')
            # Aplica a cifra de César
            novo_indice = (indice - chave) % 26
            # Converte o índice de volta para um caractere
            novo_caractere = chr(novo_indice + ord('A'))
            resultado += novo_caractere
        # Verifica se o caractere é uma letra minúscula
        elif caractere.islower():
            indice = ord(caractere) - ord('a')
            novo_indice = (indice - chave) % 26
            novo_caractere = chr(novo_indice + ord('a'))
            resultado += novo_caractere
        else:
            # Mantém o caractere inalterado (ex.: espacos, pontuacao)
            resultado += caractere
    fim = time.time()
    print(f"Tempo de execucao descriptografar cesar: {fim-inicio:.2f} segundos")

    return resultado

def descriptografarCifraAF(texto_cifrado, chave):
    inicio = time.time()
    resultado = ""
    chave_str = str(chave)  # Converte a chave para string para iterar sobre os dígitos
    tamanho_chave = len(chave_str)
    intervalo_inferior = 32
    intervalo_superior = 126
    intervalo_tamanho = intervalo_superior - intervalo_inferior + 1

    for i, caractere in enumerate(texto_cifrado):
        valor_ascii = ord(caractere)
        
        # Calcula o deslocamento com base em um dígito da chave
        deslocamento = int(chave_str[i % tamanho_chave])

        if intervalo_inferior <= valor_ascii <= intervalo_superior:
            # Subtrai o deslocamento para descriptografar
            novo_valor_ascii = intervalo_inferior + ((valor_ascii - intervalo_inferior - deslocamento) % intervalo_tamanho)
            novo_caractere = chr(novo_valor_ascii)
        else:
            novo_caractere = caractere

        resultado += novo_caractere
    fim = time.time()
    #print(f"Tempo de execucao descriptografar cifraAF: {fim-inicio:.2f} segundos")
    #print(resultado)

    return resultado

def descriptografarCifraAF2(texto_cifrado, chave):
    #inicio = time.time()
    resultado = ""
    chave_str = str(chave)  # Converte a chave para string para iterar sobre os pares de dígitos
    tamanho_chave = len(chave_str)
    intervalo_inferior = 32
    intervalo_superior = 126
    intervalo_tamanho = intervalo_superior - intervalo_inferior + 1

    for i, caractere in enumerate(texto_cifrado):
        valor_ascii = ord(caractere)

        if tamanho_chave > 1:
            # Calcula os índices para dois caracteres da chave
            indice_chave1 = (i * 2) % tamanho_chave
            indice_chave2 = (i * 2 + 1) % tamanho_chave
            
            if indice_chave2 < tamanho_chave:
                deslocamento = int(chave_str[indice_chave1] + chave_str[indice_chave2])
            else:
                deslocamento = int(chave_str[indice_chave1])  # Usa o último dígito sozinho
        else:
            deslocamento = int(chave_str)  # Para chave de um único dígito

        if intervalo_inferior <= valor_ascii <= intervalo_superior:
            novo_valor_ascii = intervalo_inferior + ((valor_ascii - intervalo_inferior - deslocamento) % intervalo_tamanho)
            novo_caractere = chr(novo_valor_ascii)
        else:
            novo_caractere = caractere

        resultado += novo_caractere
    #fim = time.time()
    #print(f"Tempo de execucao descriptografar cifraAF2: {fim-inicio:.2f} segundos")
    return resultado

def forcaBrutaAF2(textoCriptografado, textoAlvo):
    inicio = time.time()
    print("tentando forca bruta com cifra AF2...")
    i = 0
    texto=""
    while(texto!=textoAlvo):
        texto=descriptografarCifraAF2(textoCriptografado,i)
        i=i+1
    print("chave encontrada:",i-1) 
    fim = time.time()
    print(f"Tempo de execucao forca brutacom cifra AF2: {fim-inicio:.6f} segundos")

def forcaBrutaAF(textoCriptografado, textoAlvo):
    inicio = time.time()
    print("tentando forca bruta com cifra AF...")
    i = 0
    texto=""
    while texto != textoAlvo:
        texto = descriptografarCifraAF(textoCriptografado, i)
        #print(f"Tentativa {i}: {texto}")  # Debug: para ver as tentativas
        i += 1
    
    if texto == textoAlvo:
        print("Chave encontrada:", i-1)
    else:
        print("Chave não encontrada dentro do limite de tentativas.")

    fim = time.time()
    print(f"Tempo de execucao forca bruta com cifra AF: {fim-inicio:.6f} segundos")
