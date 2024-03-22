import re

# Lista de palavras reservadas
PALAVRAS_RESERVADAS = ["int", "float", "char", "boolean", "void", "if", "else",
                       "for", "while", "input", "print", "main", "return"]

# Expressões regulares para tokens
REGEX_NUM_INT = r"-?[0-9]+(?!\.)"
REGEX_NUM_DEC = r"-?[0-9]+(\.[0-9]+)?"
REGEX_ID = r"[a-zA-Z_]\w*"
REGEX_TEXTO = r'\"(.*?)\"'
REGEX_OPERADORES = r"=|\+|\-|\*|/|%|&|\||!|>=|<=|!=|=="
REGEX_SIMBOLOS_ESPECIAIS = r"[\(\)\[\]\{\},;:]"
REGEX_COMENTARIOS = r'(#.*)'

# Dicionário para mapear tokens para seus tipos
TOKEN_TIPOS = {
    "NUM_INT": "Número Inteiro",
    "NUM_DEC": "Número Decimal",
    "ID": "Identificador",
    "TEXTO": "Constante de Texto",
    "OPERADORES": "Operador",
    "SIMBOLOS_ESPECIAIS": "Símbolo Especial",
    "COMENTARIO": "Comentário",
    "PALAVRA_RESERVADA": "Palavra Reservada"
}

def analisar_lexema(lexema):
    """
    Analisa um lexema e retorna seu tipo e valor.

    Args:
        lexema: O lexema a ser analisado.

    Returns:
        Uma tupla contendo o tipo do token e seu valor.
    """
    if lexema in PALAVRAS_RESERVADAS:
        return ("PALAVRA_RESERVADA", lexema)
    elif re.match(REGEX_NUM_INT, lexema):
        # Remove trailing characters before conversion
        lexema_int = re.sub(r'[^\d-]', '', lexema) 
        return ("NUM_INT", int(lexema_int))
    elif re.match(REGEX_NUM_DEC, lexema):
        # Remove trailing characters before conversion
        lexema_dec = re.sub(r'[^\d.-]', '', lexema) 
        return ("NUM_DEC", float(lexema_dec))
    elif re.match(REGEX_ID, lexema):
        return ("ID", lexema)
    elif re.match(REGEX_TEXTO, lexema):
        return ("TEXTO", lexema[1:-1])
    elif re.match(REGEX_OPERADORES, lexema):
        return ("OPERADORES", lexema)
    elif re.match(REGEX_SIMBOLOS_ESPECIAIS, lexema):
        return ("SIMBOLOS_ESPECIAIS", lexema)
    elif re.match(REGEX_COMENTARIOS, lexema):
        return ("COMENTARIO", lexema)
    else:
        return ("ERRO", "Lexema inválido: " + lexema)




def analisar_codigo(codigo):
    """
    Analisa um código-fonte e gera uma sequência de tokens.

    Args:
        codigo: O código-fonte a ser analisado.

    Returns:
        Uma lista de tokens.
    """
    tokens = []
    lexema = ""
    in_string = False  # Indica se estamos dentro de uma string

    # Divida o código-fonte em linhas
    linhas = codigo.split("\n")

    for linha in linhas:
        # Se a linha começar com '#', considere-a como um comentário
        if linha.strip().startswith('#'):
            tokens.append(analisar_lexema(linha.strip()))
            continue

        # Loop através dos caracteres da linha
        i = 0
        while i < len(linha):
            caractere = linha[i]

            if caractere in ['"', "'"]:
                # Inverte o status de in_string quando encontramos uma aspa
                in_string = not in_string

            if not in_string and caractere in [" ", "\t"]:
                if lexema:
                    tokens.append(analisar_lexema(lexema))
                    lexema = ""
            else:
                # Verifica se o caractere é um símbolo especial
                if caractere in ['(', ')', '[', ']', '{', '}', ',', ';']:
                    if lexema:
                        tokens.append(analisar_lexema(lexema))
                        lexema = ""
                    tokens.append(analisar_lexema(caractere))
                else:
                    lexema += caractere

            i += 1

        if lexema:
            tokens.append(analisar_lexema(lexema))
            lexema = ""

    return tokens


def main():
    # Código-fonte de exemplo
    codigo = """
    def soma_numeros():
        # Solicita ao usuário que insira dois números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        num3 = 4.6
        
        # Calcula a soma dos números
        resultado = num1 + num2
        
        # Imprime a soma
        print("A soma dos dois números é:", resultado)
    def media_tres_numeros():
        # Solicita ao usuário que insira três números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        num3 = float(input("Digite o terceiro número: "))
        
        # Calcula a média dos três números
        media = (num1 + num2 + num3) / 3
        
        # Imprime a média
        print("A média dos três números é:", media)
    # Chama a função para calcular a soma dos números
    soma_numeros()
    # Chama a função para calcular a média dos três números
    media_tres_numeros()
    # Comentário de exemplo
    # Este é um comentário simples
  """

    tokens = analisar_codigo(codigo)

    # Imprimir tokens
    for token in tokens:
        tipo, valor = token
        print(f"{TOKEN_TIPOS.get(tipo, tipo)} -> {valor}")


if __name__ == "__main__":
    main()
