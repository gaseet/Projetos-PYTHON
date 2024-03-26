import re

# Lista de palavras reservadas
PALAVRAS_RESERVADAS = ["int", "float", "char", "boolean", "void", "if", "else", "def",
                       "for", "while", "input", "print", "main", "return", "try", "and", "or"]

# Expressões regulares para tokens
REGEX_NUM_INT = r"-?[0-9]+(?!\.)"
REGEX_NUM_DEC = r"-?[0-9]+(\.[0-9]+)?+(?!\.)"
REGEX_ID = r"[a-zA-Z_]\w*"
REGEX_TEXTO = r'\'(.*?)\'|\"(.*?)\"'
REGEX_OPERADORES = r"=|<|>|\+|\-|\*|/|%|&|\||!|>=|<=|!=|=="
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
        # Remove caracteres adicionais antes da conversão
        lexema_int = re.sub(r'[^\d-]', '', lexema) 
        return ("NUM_INT", int(lexema_int))
    elif re.match(REGEX_NUM_DEC, lexema):
        # Remove caracteres adicionais antes da conversão
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
    tokens = []  # Inicializa uma lista vazia para armazenar os tokens
    lexema = ""  # Inicializa uma string vazia para armazenar os lexemas temporários
    in_string = False  # Indica se estamos dentro de uma string

    # Divida o código-fonte em linhas
    linhas = codigo.split("\n")

    for linha in linhas:
        # Se a linha começar com '#', considere-a como um comentário
        if linha.strip().startswith('#'):
            tokens.append(analisar_lexema(linha.strip()))  # Analisa o comentário como um token
            continue

        # Loop através dos caracteres da linha
        i = 0
        while i < len(linha):
            caractere = linha[i]

            if caractere in ['"', "'"]:
                # Inverte o status de in_string quando encontramos uma aspa
                in_string = not in_string
                lexema += caractere

            elif in_string:
                lexema += caractere

                # Verifica se terminamos uma string
                if len(lexema) >= 2 and lexema[0] == lexema[-1]:
                    tokens.append(analisar_lexema(lexema))  # Analisa a string como um token
                    lexema = ""  # Limpa o lexema temporário
                    in_string = False  # Reinicia o status de string

            elif caractere in [" ", "\t", "(", ")", "[", "]", "{", "}", ",", ";", ":"]:
                if lexema:
                    tokens.append(analisar_lexema(lexema))  # Analisa o lexema temporário como um token
                    lexema = ""  # Limpa o lexema temporário
                if caractere.strip():
                    tokens.append(analisar_lexema(caractere))  # Analisa caracteres especiais como tokens separados

            else:
                lexema += caractere  # Adiciona o caractere ao lexema temporário

            i += 1

        if lexema:
            tokens.append(analisar_lexema(lexema))  # Analisa o lexema final da linha como um token
            lexema = ""  # Limpa o lexema temporário

    return tokens  # Retorna a lista de tokens gerada


def main():
    # Código-fonte a ser analisado
    codigo = """
    def verificar_idade(idade):
            if idade >= 18:
                return "Maior de idade"
            else:
                return "Menor de idade"

    def main():
            try:
                idade = int(input("Digite sua idade: "))
                resultado = verificar_idade(idade)
                print(resultado)
            except ValueError:
                print("Por favor, digite um número válido para a idade.")

    if __name__ == "__main__":
        main()
  """

    tokens = analisar_codigo(codigo)

    # Imprimir tokens
    for token in tokens:
        tipo, valor = token
        print(f"{TOKEN_TIPOS.get(tipo, tipo)} -> {valor}")


if __name__ == "__main__":
    main()
