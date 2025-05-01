import streamlit as st
from PIL import Image

st.title("Equipos de Fórmula 1")

st.header("¿Qué son los equipos de F1?")
st.write("""
En la Fórmula 1, cada equipo (también llamado escudería) es responsable de diseñar, construir y operar sus propios autos de carrera. 
Cada equipo tiene dos pilotos y compite por el **Campeonato de Constructores**, mientras que los pilotos luchan por el **Campeonato de Pilotos**.

Los equipos tienen identidades visuales fuertes, con colores, patrocinadores y estilos únicos.
""")

# Imagen general de equipos
st.subheader("La parrilla actual")
imagen_parrilla = Image.open("imagenparrillaequipos.jpg")  # Personaliza esta imagen
st.image(imagen_parrilla, caption="Autos de los equipos actuales en la parrilla", use_container_width=True)

st.header("Equipos destacados de la temporada")

# Red Bull Racing
st.subheader("Red Bull Racing")
st.write("""
Dominante en los últimos años, Red Bull es conocido por su diseño aerodinámico innovador y su agresiva estrategia de carrera. 
Sus colores son el azul oscuro con detalles en rojo y amarillo.
""")
imagen_redbull = Image.open("imagenredbull.jpg")
st.image(imagen_redbull, caption="Monoplaza de Red Bull Racing", use_container_width=True)

# Ferrari
st.subheader("Scuderia Ferrari")
st.write("""
El equipo más icónico y antiguo de la F1. Con sede en Italia, Ferrari es conocido por su característico color rojo y su historia llena de gloria y pasión.
""")
imagen_ferrari = Image.open("imagenferrari.jpg")
st.image(imagen_ferrari, caption="Ferrari: pasión y tradición", use_container_width=True)

# Mercedes
st.subheader("Mercedes-AMG Petronas")
st.write("""
Mercedes dominó la F1 durante la era híbrida con múltiples campeonatos consecutivos. Su auto es reconocido por su color plateado con detalles en verde agua.
""")
imagen_mercedes = Image.open("imagenmercedes.jpg")
st.image(imagen_mercedes, caption="El auto plateado de Mercedes", use_container_width=True)

# McLaren
st.subheader("McLaren")
st.write("""
Uno de los equipos más históricos, McLaren ha regresado con fuerza en temporadas recientes. Su color papaya es distintivo en la pista.
""")
imagen_mclaren = Image.open("imagenmclaren.jpg")
st.image(imagen_mclaren, caption="McLaren papaya en acción", use_container_width=True)

st.markdown("---")
st.caption("Existen muchos otros equipos en la parrilla como Alpine, Aston Martin, Haas, Alfa Romeo, AlphaTauri y Williams.")
