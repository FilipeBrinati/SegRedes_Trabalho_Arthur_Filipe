import time
from criptografia import cifraCesar, cifraAF, cifraAF2
from analise import forcaBrutaAF, forcaBrutaAF2, DescriptografacifraCesar, descriptografarCifraAF , descriptografarCifraAF2

# Funcao principal
def executar_criptografias(texto, chaves):

    
    for i, chave in enumerate(chaves):
        print(f"Execucao {i+1} com chave: {chave}")
        
        # Cifra de César
        print("/////// Cifra César /////////")
        start = time.time()  # Inicia a medicao de tempo
        texto_criptografado = cifraCesar(texto, chave)
        descrip = DescriptografacifraCesar(texto_criptografado, chave)
        end = time.time()  # Termina a medicao de tempo
        tempo_cesar = end - start
        print(f"Tempo de execucao: {tempo_cesar:.6f} segundos")
        
        # Cifra AF
        print("/////// Cifra AF /////////")
        start = time.time()
        texto_criptografado = cifraAF(texto, chave)
        descrip = descriptografarCifraAF(texto_criptografado, chave)
        end = time.time()
        tempo_af = end - start
        print(f"Tempo de execucao: {tempo_af:.6f} segundos")

        # Forca Bruta para Cifra AF
        print("/////// FORcA BRUTA PARA Cifra AF /////////")
        forcaBrutaAF(texto_criptografado, texto)
        print("///////////////////////")
        print()
        
        # Cifra AF2
        print("/////// Cifra AF2 /////////")
        start = time.time()
        texto_criptografado = cifraAF2(texto, chave)
        descrip = descriptografarCifraAF2(texto_criptografado, chave)
        end = time.time()
        tempo_af2 = end - start
        print(f"Tempo de execucao: {tempo_af2:.6f} segundos")

        # Forca Bruta para Cifra AF2
        print("/////// FORcA BRUTA PARA Cifra AF2 /////////")
        forcaBrutaAF2(texto_criptografado, texto)
        print("///////////////////////")
        print()


# Caminho do arquivo (no mesmo diretório do script)
nome_arquivo = 'texto.txt'
try:
    with open(nome_arquivo, 'r') as arquivo:
        texto = arquivo.read()
except FileNotFoundError:
    print(f"Arquivo '{nome_arquivo}' não encontrado. Tentando caminho alternativo...")
    nome_arquivo = 'src/texto.txt'
    try:
        with open(nome_arquivo, 'r') as arquivo:
            texto = arquivo.read()
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' também não foi encontrado.")

# Definicao das chaves
chaves = [2, 50, 431, 6782, 54328, 987653, 4287561]

# Executar com 7 chaves diferentes e capturar os tempos
executar_criptografias(texto, chaves)
