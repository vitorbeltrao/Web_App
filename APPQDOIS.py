# Import the necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("https://raw.githubusercontent.com/vitorbeltrao/Datasets/main/QDOIS_intergalaxy_sales%20(2).csv")

# Título
st.title('QDOIS Galaxy Company')

# Subtítulo
st.header('Exploratory Data Analysis')

# subsubtitulo
st.subheader("Web app for internal consumption of the QDOIS Galaxy team")

# Tabela de dados
df["date"] = pd.to_datetime(df["date"])
df['Year-Week'] = df['date'].dt.strftime('%Y-%U')


# Carregando os dados
labels_1 = df.date.unique().tolist()
labels_2 = df.price.unique().tolist()
labels_3 = df.planet.unique().tolist()
labels_4 = df['product'].unique().tolist()
labels_5 = df['Year-Week'].unique().tolist()

# INICIO DO SIDEBAR
# Parâmetros
st.sidebar.header("Parameters")

# Slider de seleção do ano
st.sidebar.subheader("Data")
year_to_filter = st.sidebar.slider("Choose the desired year", 2007, 2019, 2013)

# Checkbox da tabela
st.sidebar.subheader("Table")
tabela = st.sidebar.empty()

# multiselect com os labels únicos
label_to_filter_1 = st.sidebar.multiselect(
    label= "Choose the desired planet",
    options= labels_3,
    default = labels_3
)

label_to_filter_2 = st.sidebar.multiselect(
    label= "Choose the desired product",
    options= labels_4,
    default = labels_4
)

# Somente aqui os dados filtrados por ano são atualizados em um novo dataframe
filtered_df = df[(df.date.dt.year == year_to_filter) & (df.planet.isin(label_to_filter_1)) &
                 (df['product'].isin(label_to_filter_2))]
# ACABOU O SIDEBAR

# INICIO DO CORPO DO DASHBOARD
# raw data (tabela) dependente do checkbox
if tabela.checkbox("Show data table"):
    st.write(filtered_df)

#  Gráfico total de vendas por ano
grouping_year = df.groupby(df['date'].dt.year)['price'].sum()
st.write("Total sales per year (Year x Price)")
st.bar_chart(grouping_year)

#  Gráfico total de vendas por produto e planeta
fig, ax = plt.subplots(figsize=(12,5))
sns.countplot('product', data=df, ax=ax, hue='planet')
st.write('Total Sales per product and planet')
st.pyplot(fig)

# time series
grouping_year = df.groupby(df['date'].dt.year)['price'].sum()
st.write("Time series (Year x Price)")
st.line_chart(grouping_year)

# products
grouping_year = df.groupby(df['product'])['price'].sum()
st.write("Total sales per product (Product x Price)")
st.bar_chart(grouping_year)

# planets
grouping_year = df.groupby(df['planet'])['price'].sum()
st.write("Total sales per product (Planet x Price)")
st.bar_chart(grouping_year)