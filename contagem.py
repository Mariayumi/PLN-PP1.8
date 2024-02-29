from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from collections import Counter
import re

import nltk
nltk.download('stopwords')

## stopwords = palavras que ocorrem com muita frequência, mas geralmente não contribuem significativamente para o conteúdo semântico de um texto

# r = read
with open('texto.txt', 'r', encoding='utf-8') as file:
    cinderela = file.read()

# [:5] = slicing
print(cinderela[:5]);

#re.findall = encontra todas as ocorrências de um padrão em uma string e retorna uma lista com todas as correspondências encontradas
palavras = re.findall(r'\b\w+\b', cinderela);
contagem = Counter(palavras);

stop_words = set(stopwords.words('english'));
stopwords_cinderela =  [word.lower() for word in palavras if word.lower() not in stop_words];
cinderela_clean = Counter(stopwords_cinderela);

# most_common(n) = organiza as n palavras que mais repetem
comum = contagem.most_common(10);
comum_sem_sw = cinderela_clean.most_common(10);

# zip() = separa as palavras das quantidades em duas listas imutáveis
palavra, quantidade = zip(*comum);
palavra_sem_sw, quantidade_sem_sw = zip(*comum_sem_sw);

total = sum(contagem.values())
print(f"O total de palavras no texto é: {total}")

print() 

print("As 10 palavras mais recorrentes são:")
print("Palavra  | Repetições")
print("--------------------")
for word, count in zip(palavra, quantidade):
    print(f"{word.ljust(8)} | {count}")

print() 
print() 

total_sem_stopwords = len(cinderela_clean)
print(f"O total de palavras no texto sem stopwords é: {total_sem_stopwords}")

print() 

print("As 10 palavras mais recorrentes sem stopwords são:")
print("Palavra  | Repetições")
print("--------------------")
for word, count in zip(palavra_sem_sw, quantidade_sem_sw):
    print(f"{word.ljust(8)} | {count}")

plt.figure(figsize=(20, 6))

plt.subplot(1, 2, 1)  
plt.bar(palavra, quantidade, color='#ad7ef9')
plt.xlabel('Palavras')
plt.ylabel('Contagem de repetições')
plt.title('Top 10 Palavras Mais Comuns')
plt.xticks(rotation=45, ha='right')

plt.subplot(1, 2, 2) 
plt.bar(palavra_sem_sw, quantidade_sem_sw, color='#ff7682')
plt.xlabel('Palavras')
plt.ylabel('Contagem de repetições')
plt.title('Top 10 Palavras Mais Comuns sem Stopwords')
plt.xticks(rotation=45, ha='right')

plt.tight_layout() 
plt.show()