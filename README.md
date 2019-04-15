# string2num

## Descrição
Classe que permite converter números escritos por extenso para suas respectivas formas numéricas. Possui funções de conversão de string para float e string para forma monetária. Por enquanto está apenas disponível em pt-BR.

## Motivação
Meu trabalho ia bem até eu precisar converter um valor monetário que estava escrito em string para suas forma numérica. Pesquisando, percebi que não havia nenhum pacote ou código que fizesse isto. Tendo isto em vista, resolvi criar uma classe que tivesse diversas funcionalidades com este propósito. Além disto, há elementos de NLP para correção ortográfica de valores por extensos que forem escritos de formas erradas, possibilitando que o algoritmo possa identificá-los.

## Uso

```python
from config import *
from extenso2numero import *

frase = "trinta e cinco reais e quarenta e três centavos"
currencyconverter(frase, numDict, milharDict, resultado, grupo)
```
## Exemplo de uso mostrando NLP
![alt text](https://github.com/ClaDavid/string2num/blob/master/string2numexample.png "string2num example usage")

### EM CONSTRUÇÃO
