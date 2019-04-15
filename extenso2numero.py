# Author: Clarissa David
import re
import enchant
from enchant.checker import SpellChecker

def spellcorrect(string_extenso):
    checker_spell = enchant.checker.SpellChecker("pt_BR")
    checker_spell.set_text(string_extenso)
    for err in checker_spell:
    	suggestion = err.suggest()[0]
    	err.replace(suggestion)
    return checker_spell.get_text()

def converter(string_extenso, numDict, milharDict, resultado, grupo):
    for word in string_extenso.split():            
        if(word in numDict):
            grupo += numDict[word]
        elif(word in milharDict):
            resultado += (1 if grupo == 0 else grupo) * milharDict[word]
            grupo = 0
    resultado += grupo
    return resultado

def currencyconverter(string_extenso, numDict, milharDict, resultado, grupo):
    string_numerico = spellcorrect(string_extenso)
    frase_clean = re.sub(r'\s+e\s+|centavo(s)?', ' ', string_numerico)
    frase_plural = re.sub(r'real', 'reais', frase_clean)
    lista_currency = frase_plural.split("reais",1)
    valor_convertido = [converter(valor_extenso, numDict, milharDict, resultado, grupo) for valor_extenso in lista_currency]
    valor_join = ','.join(str(element) for element in valor_convertido)
    return valor_join
