import pandas as pd
import numpy as np
import string
import streamlit as st


df = pd.read_excel(r"C:\Users\User\Desktop\case tecnico - maxmilhas\case_dados_2.xlsx",engine="openpyxl", sheet_name="BaseItens")

def main():
  st.markdown("<h1 style='text-align: center; color: White;background-color:#3b5998'>Dashboard MaxMilhas</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='text-align: center; color: Black;'>Métricas de Acompanhamento dos Resultados</h3>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: center; color: Black;'> 1. Análises de Frequências nos Aeroportos:</h4>", unsafe_allow_html=True)
  st.sidebar.header("Sobre o Web App:")
  st.sidebar.write("App para consumo interno da MaxMilhas com o objetivo de acompanhar algumas métricas de resultados.")
  st.sidebar.write("Não se esqueça de verificar também a análise exploratória completa no notebook.")

  # Checkbox da tabela
  st.sidebar.subheader("Tabela de dados:")
  tabela = st.sidebar.empty()

  # raw data (tabela) dependente do checkbox
  if tabela.checkbox("Exibir Dataset"):
      st.write(df)

if __name__ == '__main__':
    main()

# Corpo do dashboard
#############################################################################################
# Tabela de frequências - 1
frequencia = df['from_iata'].value_counts()
porcentagem = df['from_iata'].value_counts(normalize = True) * 100
dist_freq_from = pd.DataFrame({'Frequência': frequencia, 'Porcentagem (%)': porcentagem})
# Análise gráfica
st.write("Gráfico dos locais que saem voos - (Aeroporto x Quantidade)")
st.bar_chart(frequencia)
# Checkbox da tabela
st.sidebar.subheader("Tabelas de frequências:")
tabela = st.sidebar.empty()
if tabela.checkbox("Frequencia dos locais que saem voos"):
  st.write(dist_freq_from)
#############################################################################################
# Tabela de frequências - 2
frequencia_2 = df['to_iata'].value_counts()
porcentagem_2 = df['to_iata'].value_counts(normalize = True) * 100
dist_freq_to = pd.DataFrame({'Frequência': frequencia_2, 'Porcentagem (%)': porcentagem_2})
# Análise gráfica
st.write("Gráfico dos locais que chegam voos - (Aeroporto x Quantidade)")
st.bar_chart(frequencia_2)
# Checkbox da tabela
tabela = st.sidebar.empty()
if tabela.checkbox("Frequencia dos locais que chegam voos"):
  st.write(dist_freq_to)
#############################################################################################
st.markdown("<h4 style='text-align: center; color: Black;'> 2. Análises das Receitas Geradas e Milhas Utilizadas por ID do Status:</h4>", unsafe_allow_html=True)
#############################################################################################
# Tabela da receita com o ID do status - 3
valores_agrupados = df.groupby(df['status_id'])['valor_passagem'].sum()
valor_total = df.valor_passagem.values.sum()
porcentagem = (valores_agrupados/valor_total)*100
tabela_3 = pd.DataFrame({'Valor':valores_agrupados, 'Porcentagem (%)': porcentagem})
# Análise gráfica
st.write("Gráfico de receita por ID do status - (ID status x R$)")
st.bar_chart(valores_agrupados)
# Checkbox da tabela
tabela = st.sidebar.empty()
if tabela.checkbox("Tabela de receita por ID do status"):
  st.write(tabela_3)
#############################################################################################
# Tabela de milhas com o ID do status - 4
valores_agrupados_2 = df.groupby(df['status_id'])['milhas_usadas'].sum()
valor_total_2 = df.milhas_usadas.values.sum()
porcentagem_2 = (valores_agrupados_2/valor_total_2)*100
tabela_4 = pd.DataFrame({'Qtde. Milhas':valores_agrupados_2, 'Porcentagem (%)': porcentagem_2})
# Análise gráfica
st.write("Gráfico das milhas utilizadas por ID do status - (ID status x Qtde. Milhas)")
st.bar_chart(valores_agrupados_2)
# Checkbox da tabela
tabela = st.sidebar.empty()
if tabela.checkbox("Tabela das milhas utilizadas por ID do status"):
  st.write(tabela_4)
#############################################################################################
st.markdown("<h4 style='text-align: center; color: Black;'> 3. Receita Efetiva por Aeroportos:</h4>", unsafe_allow_html=True)
#############################################################################################
# Tabela de receita para aeroportos que saem voos - 5
# filtrando o dataframe
df_filtrado = df.loc[(df["status_id"]==1),
["status_id","from_iata","to_iata", "valor_passagem", "milhas_usadas"]]
valores_agrupados_3 = df_filtrado.groupby(df['from_iata'])['valor_passagem'].sum()
valor_total_3 = df_filtrado.valor_passagem.values.sum()
porcentagem_3 = (valores_agrupados_3/valor_total_3)*100
tabela_5 = pd.DataFrame({'Valor':valores_agrupados_3, 'Porcentagem (%)': porcentagem_3})
# Análise gráfica
st.write("Gráfico da receita efetiva gerada por aeroportos (Aeroporto Origem x R$)")
st.bar_chart(valores_agrupados_3)
# Checkbox da tabela
tabela = st.sidebar.empty()
if tabela.checkbox("Tabela da receita efetiva por aeroporto origem"):
  st.write(tabela_5)
#############################################################################################
# Tabela de receita para aeroportos que chegam voos - 6
valores_agrupados_4 = df_filtrado.groupby(df['to_iata'])['valor_passagem'].sum()
valor_total_4 = df_filtrado.valor_passagem.values.sum()
porcentagem_4 = (valores_agrupados_4/valor_total_4)*100
tabela_6 = pd.DataFrame({'Valor':valores_agrupados_4, 'Porcentagem (%)': porcentagem_4})
# Análise gráfica
st.write("Gráfico da receita efetiva gerada por aeroportos (Aeroporto Destino x R$)")
st.bar_chart(valores_agrupados_4)
# Checkbox da tabela
tabela = st.sidebar.empty()
if tabela.checkbox("Tabela da receita efetiva por aeroporto destino"):
  st.write(tabela_5)
#############################################################################################
