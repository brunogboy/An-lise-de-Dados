#!/usr/bin/env python
# coding: utf-8

# In[1]:


dados = {'Semanas': [1, 2, 3, 4],
        'Produto': ['Brinquedo', 'Lego', 'Massinha', 'Boneca'],
        'Preço Unit': ['R$80.00','R$123.00','R$19.00', 'R$110.00'],
        'Qtnd Vendida': [31,54, 23, 103]}


# In[2]:


# Instala a versão exata do pacote
get_ipython().system('pip install -q matplotlib==3.7.1')


# In[3]:


import matplotlib as mpl


# In[4]:


# O matplotlib.pyplot é uma coleção de funções e estilos do Matplotlib 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


from pandas import DataFrame


# In[6]:


df = DataFrame(dados)


# In[7]:


print("Olá Chefe, tudo bem? Segue a tabela de vendas do Mês, por semana:\n ")


# In[8]:


print(df.head())


# In[13]:


escolha1 = input("Chefe, escolha o que precisa saber sobre essa tabela:\n 1. Produto mais vendido\n 2. Produto menos vendido\n 3. Média de venda no mês\n 4. Mostrar um gráfico geral\n")

if escolha1 == '1':
    indice_produto_mais_vendido = dados['Qtnd Vendida'].index(max(dados['Qtnd Vendida']))
    produto_mais_vendido = dados['Produto'][indice_produto_mais_vendido]
    quantidade_vendida = dados['Qtnd Vendida'][indice_produto_mais_vendido]
    print(f'O produto mais vendido foi "{produto_mais_vendido}" com {quantidade_vendida} unidades vendidas.')
elif escolha1 == '2':
    indice_produto_menos_vendido = dados['Qtnd Vendida'].index(min(dados['Qtnd Vendida']))
    produto_menos_vendido = dados['Produto'][indice_produto_menos_vendido]
    quantidade_vendidamin = dados['Qtnd Vendida'][indice_produto_menos_vendido]
    print(f'O produto menos vendido foi "{produto_menos_vendido}" com {quantidade_vendidamin} unidades vendidas.')
elif escolha1 == '3':
    media_vendas = sum(dados['Qtnd Vendida']) / len(dados['Qtnd Vendida'])
    print(f'A média de vendas é de {media_vendas:.2f} unidades por produto.')
elif escolha1 == '4':
    # Criando o gráfico de barras
    plt.bar(dados['Produto'], dados['Qtnd Vendida'])
    plt.xlabel('Produto')
    plt.ylabel('Quantidade Vendida')
    plt.title('Vendas por Produto')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("Digite um dos números acima!")
print("\nAgradeço pela confiança, chefe! Melhorando cada dia mais!! :)")


# In[ ]:




