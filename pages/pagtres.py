import streamlit as st
from PIL import Image

st.title("Pilotos de Fórmula 1")

st.header("¿Quiénes son los pilotos de la F1?")
st.write("""
Los **pilotos de Fórmula 1** son atletas de élite altamente entrenados, capaces de controlar vehículos a más de 300 km/h con precisión milimétrica. Cada equipo tiene generalmente dos pilotos titulares que compiten a lo largo de toda la temporada.

Los pilotos deben tener una **licencia de superpiloto** otorgada por la FIA y demostrar no solo habilidad técnica, sino también resistencia física y mental excepcionales.
""")

# Imagen general de pilotos
st.subheader("Pilotos en la parrilla")
image_pilotos = Image.open("imagenpilotosactuales.jpg")  # reemplázala con tu imagen
st.image(image_pilotos, caption="Pilotos actuales de la Fórmula 1", use_container_width=True)

st.header("Pilotos actuales destacados")
st.write("""
Algunos de los pilotos más destacados en la actual parrilla son:

- **Max Verstappen** (Red Bull Racing): Campeón mundial con un estilo agresivo y gran consistencia.
- **Lewis Hamilton** (Mercedes): Uno de los más exitosos de todos los tiempos, con 7 campeonatos mundiales.
- **Charles Leclerc** (Ferrari): Conocido por su talento natural y velocidad en clasificación.
- **Fernando Alonso** (Aston Martin): Veterano con dos títulos mundiales y gran experiencia.
""")

# Imagen de Max Verstappen
st.subheader("Max Verstappen")
image_verstappen = Image.open("imagenverstappen.jpg")
st.image(image_verstappen, caption="Max Verstappen en acción", use_container_width=True)

st.header("Pilotos legendarios de la historia")
st.write("""
A lo largo de los años, la Fórmula 1 ha visto pilotos legendarios que marcaron época, como:

- **Ayrton Senna** (Brasil): Tres veces campeón, recordado por su pasión y talento en pista mojada.
- **Michael Schumacher** (Alemania): Siete veces campeón, dominó con Ferrari en los 2000.
- **Niki Lauda**, **Alain Prost**, **Juan Manuel Fangio**: íconos que ayudaron a construir la historia del deporte.
""")

# Imagen de Senna
st.subheader("Ayrton Senna")
image_senna = Image.open("imagensenna.jpg")
st.image(image_senna, caption="Ayrton Senna, una leyenda de la F1", use_container_width=True)

st.markdown("---")
st.caption("Puedes seguir a tus pilotos favoritos en las redes sociales o en la app oficial de la F1.")
