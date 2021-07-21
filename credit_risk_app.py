import pandas as pd
import numpy as np
import string
import pickle
import streamlit as st

model = pickle.load(open('new_model.pkl','rb'))

def main():
  st.markdown("<h1 style='text-align: center; color: White;background-color:#e84343'>Predição de Risco de Crédito</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='text-align: center; color: Black;'>Coloque as entradas necessárias e nós faremos o resto.</h3>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: center; color: Black;'>by Vítor Beltrão</h4>", unsafe_allow_html=True)
  st.sidebar.header("Sobre o app:")
  st.sidebar.write("App de predição para empresas que queiram analisar o risco de empréstimo para os clientes.")
  st.sidebar.header("Banco de dados:")
  st.sidebar.write("A aquisição dos dados foi feita pelo kaggle.")

  # part of our main method
  income = st.slider("Selecione o valor da sua renda:", 1000, 100000, 50000)
  age = st.slider("Selecione a sua idade:", 18, 65, 42)
  loan = st.slider("Selecione o valor do empréstimo:", 0, 7500, 100000)

  inputs = [[income, age, loan]]  # our inputs

  if st.button('Predict'):  # making and printing our prediction
      result = model.predict(inputs)
      updated_res = result.flatten().astype(float)
      st.success('Resultado do modelo: {}'.format(updated_res))

if __name__ == '__main__':
    main()  # calling the main method

st.write("1: Emprèstimo negado.")
st.write("0: Emprèstimo aprovado.")

