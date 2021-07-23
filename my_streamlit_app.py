# Ouvrir le terminal Anaconda Prompt
# Installer streamlit : pip install streamlit
# Se déplacer dans le répertoire des scripts Python : cd Documents\Python_Scripts
# Lancer le script Python : streamlit run my_streamlit_app.py


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Welcome to my application! 👋')

# Afficher un élément : st.write
st.title("Analyzing Car Data")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)


#--------------------------------------------------------------------
# checkbox widget pour visualiser ou non le dataset (partie gauche)
#checkbox = st.sidebar.checkbox("Show data")
#print(checkbox)
#if checkbox:
#    st.write("Dataset : ")
#    df
#--------------------------------------------------------------------

# checkbox pour visualiser ou non le dataset (partie droite)
checkbox = st.checkbox("Show Dataset")
print(checkbox)
if checkbox:
    df

#--------------------------------------------------------------------
# Affichage des graphiques :
#st.sidebar.subheader("Scatterplot setup")
# numeric_columns = df.select_dtypes(['float64', 'int64']).columns

# add select widget
#box1 = st.sidebar.selectbox(label="X axis", options = numeric_columns)
#box2 = st.sidebar.selectbox(label="Y axis", options = numeric_columns)

# Scatterplot
#st.write("Scatterplot : ")
#fig10 = sns.relplot(x = box1, y = box2, data = df)
#st.pyplot(fig10)
#----------------------------------------------------------------------

#############################
## Analyse de correlation ##
#############################

st.title("Correlation Analysis")

# Choix de la mesure/ Selectbox
st.header("Choice of the measure")
measures = df.select_dtypes(['float64', 'int64']).columns

# Scatterplot
plt.figure()
scatter_x = st.selectbox('X axis :', measures)
scatter_y = st.selectbox('Y axis :', measures)
sns.scatterplot(x=scatter_x, y=scatter_y, data=df)
plt.title("Scatterplot")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Choix du continent / Selectbox
st.header("Choice of the continent")
continent_choice = st.selectbox("Choose a continent :", df["continent"].unique())
df_choice = df[df["continent"]==continent_choice]

# Scatterplot
plt.figure()
sns.scatterplot(x=scatter_x, y=scatter_y, data=df_choice)
st.pyplot()


# Correlation positive
st.header("Example of a positive correlation")
plt.figure()
fig1, ax1 = plt.subplots()
ax1.scatter(x = "weightlbs", y = "cubicinches", data = df)
plt.xlabel("weightlbs")
plt.ylabel("cubicinches")
plt.title("Weight and displacement")
st.pyplot(fig1)

st.write("Nous observons une corrélation positive : les 2 variables évoluent dans le même sens.")

# Correlation négative
st.header("Example of a negative correlation")
plt.figure()
fig2, ax2 = plt.subplots()
ax2.scatter(x = "weightlbs", y = "mpg", data = df)
plt.xlabel("weightlbs")
plt.ylabel("mpg")
plt.title("Weight and mpg")
st.pyplot(fig2)

st.write("Nous observons une corrélation négative : lorsque la variable weightlbs augmente, la variable mpg diminue.")


#############################
## Analyse de distribution ##
#############################

st.title("Distribution Analysis")

# Choix de la mesure/ Radio Button
st.header("Choice of the measure")
radio_choice = st.radio("Choose a measure :", measures)

# Boxplot et Histogram à côté
plt.figure()
plt.subplots(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.boxplot(x = radio_choice, y = "continent", data = df)
plt.title("Boxplot")

plt.subplot(1, 2, 2)
sns.distplot(df[radio_choice])
plt.title("Histogram")
st.pyplot()

# Choix du continent / Radio Button
st.header("Choice of the continent")
cont_choice = st.radio("Choose a continent :", df["continent"].unique())
df_cont = df[df["continent"]==cont_choice]

# Boxplot et Histogram à côté
plt.figure()
plt.subplots(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.boxplot(x = radio_choice, y = "continent", data = df_cont)
plt.title("Boxplot")

plt.subplot(1, 2, 2)
sns.distplot(df_cont[radio_choice])
plt.title("Histogram")
st.pyplot()

# Exemple Boxplot
st.header("Example : Horsepower Boxplot in Europe ")
df_eur = df[df["continent"]==" Europe."]
plt.figure()
sns.boxplot(x = "hp", y = "continent", data = df_eur)
plt.title("Boxplot")
st.pyplot()

st.write("Nous observons : une médiane vers 80, un minimum vers 50, un maximum vers 120 ainsi qu'un outlier dans les hautes valeurs.")
st.write("Visualisation des données après avoir filtré le dataset sur le continent Europe :")
st.write(df_eur.describe())

# Exemple Histogram
st.header("Example : Horsepower Histogram in Europe")
plt.figure()
sns.distplot(df_eur["hp"])
plt.title("Histogram")
st.pyplot()

st.write("Il ne s'agit pas d'une loi normale.")

# La vidéo qui explique tout!
# https://www.youtube.com/watch?v=otsQ4Q8L7gs