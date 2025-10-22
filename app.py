import streamlit as st
from PIL import Image

st.title(" Meine erste App!!")

st.header("Dies ist der Anfang und der Ort, an dem ich meine Anwendungen für multimodale Schnittstellen entwickeln kann.")
st.write("Ich kann problemlos Backend und Frontend erstellen ;).")
image = Image.open('INtro.jpg')

st.image(image, caption='Multimodale Schnittstellen')


texto = st.text_input('Schreib etwas', 'Schreiben')
st.write('Der geschriebene Text ist', texto)

st.subheader("Verwenden wir nun 2 Spalten")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Erste Spalte")
    st.write("Multimodale Schnittstellen verbessern das Benutzererlebnis")
    resp = st.checkbox('Ich stimme zu.')
    if resp:
       st.write('Richtig!')
  
with col2:
    st.subheader("Dies ist die zweite Kolumne.")
    modo = st.radio("Welche Modalität ist die wichtigste in Ihrer Schnittstelle?", ('taktil', 'auditiv', 'taktil'))
    if modo == 'taktil':
       st.write('La vista es fundamental para tu interfaz')
    if modo == 'auditiv':
       st.write('La audición es fundamental para tu interfaz')
    if modo == 'taktil':
       st.write('El tacto es fundamental para tu interfaz')
        
st.subheader("Uso de Botones")
if st.button('Presiona el botón'):
    st.write('Gracias por presionar')
else:
    st.write('No has presionado aún')

st.subheader("Selectbox")
in_mod = st.selectbox(
    "Selecciona la modalidad",
    ("Audio", "Visual", "Háptico"),
)
if in_mod == "Audio":
    set_mod = "Reproducir audio"
elif in_mod == "Visual":
    set_mod = "Reproducir video"
elif in_mod == "Háptico":
    set_mod = "Activar vibración"
st.write(" La acción es:" , set_mod)


with st.sidebar:
    st.subheader("Configura la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva","Háptica")
    )
