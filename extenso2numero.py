# Author: Clarissa David

## Importacao de bibliotecas
import re
import enchant
from enchant.checker import SpellChecker

def spellcorrect(string_extenso):
    """
    Descricao: funcao responsavel por corricao ortegrafica
    Input:
        arg1:
        tipo: str
        representa: string com numerico por extenso

    Output:
        out1:
        tipo: str
        representa: string com o numerico por extenso correto
    """
    checker_spell = enchant.checker.SpellChecker("pt_BR")
    checker_spell.set_text(string_extenso)
    for err in checker_spell:
    	suggestion = err.suggest()[0]
    	err.replace(suggestion)
    return checker_spell.get_text()

def converter(string_extenso, numDict, milharDict, resultado, grupo):
    """
    Descricao: funcao responsavel por converter string por extenso para numerico
    Input:
        arg1:
        tipo: str
        representa: string por com numero por extenso
        ----
        arg2:
        tipo: dict
        representa: dicionario com os numeros dezenas e centezas do alfabeto pt-BR
        ----
        arg3:
        tipo: dict
        representa: dicionario com os numeros milhares do alfabeto pt-BR
        ----
        arg4:
        tipo: num
        representa: numerico para adicionar o resultado
        ----
        arg5:
        tipo: num
        representa: numerico para adicionar o grupo ao qual o numerico esta

    Output:
        out1:
        tipo: num
        representa: numerico resultante da conversao da string por extenso
    """
    for word in string_extenso.split():            
        if(word in numDict):
            grupo += numDict[word]
        elif(word in milharDict):
            resultado += (1 if grupo == 0 else grupo) * milharDict[word]
            grupo = 0
    resultado += grupo
    return resultado

def currencyconverter(string_extenso, numDict, milharDict, resultado, grupo, simbolo=""):
    """
    Descricao: funcao responsavel por converter string por extenso para monetario
    Input:
        arg1:
        tipo: str
        representa: string por com valor monetario por extenso
        ----
        arg2:
        tipo: dict
        representa: dicionario com os numeros dezenas e centezas do alfabeto pt-BR
        ----
        arg3:
        tipo: dict
        representa: dicionario com os numeros milhares do alfabeto pt-BR
        ----
        arg4:
        tipo: num
        representa: numerico para adicionar o resultado
        ----
        arg5:
        tipo: num
        representa: numerico para adicionar o grupo ao qual o numerico esta

    Output:
        out1:
        tipo: num
        representa: numerico resultante da conversao da string por extenso
    """
    #string_numerico = spellcorrect(string_extenso)
    if("reais" not in string_extenso):
        string_extenso = "zero reais e " + string_extenso
    frase_clean = re.sub(r'\s+e\s+|centavo(s)?', ' ', string_extenso)
    frase_plural = re.sub(r'real', 'reais', frase_clean)
    lista_currency = frase_plural.split("reais",1)
    valor_convertido = [converter(valor_extenso, numDict, milharDict, resultado, grupo) for valor_extenso in lista_currency]
    valor_convertido[1] = "{:02d}".format(valor_convertido[1]) #coloca 0 na frente de numeros com menos de 2 digitos
    valor_join = ','.join(str(element) for element in valor_convertido)
    return simbolo + valor_join

    
