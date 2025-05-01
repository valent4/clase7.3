import streamlit as st
from PIL import Image

# Título de la página
st.title("Generalidades de la Fórmula 1")

# Sección 1: ¿Qué es la Fórmula 1?
st.header("¿Qué es la Fórmula 1?")
st.write("""
La **Fórmula 1** es la categoría más alta de automovilismo a nivel mundial. Es una serie de carreras de coches, conocida por su velocidad, tecnología avanzada y por los equipos más prestigiosos del mundo. Cada temporada, los mejores pilotos compiten en una serie de eventos conocidos como **Gran Premios**, que se celebran en circuitos de todo el mundo.
""")

# Mostrar la imagen del logo de Fórmula 1 (archivo local)
st.subheader("Logo de la Fórmula 1")
image_logo = Image.open("logof1.png")  # Asegúrate de tener esta imagen en el directorio
st.image(image_logo, caption="Logo oficial de la Fórmula 1", width=400)

# Sección 2: ¿Cómo funciona la Fórmula 1?
st.header("¿Cómo funciona la Fórmula 1?")
st.write("""
La Fórmula 1 se compone de una serie de carreras en las que los pilotos deben completar un número determinado de vueltas en un circuito. Cada carrera tiene un **gran premio** en el que los pilotos compiten por sumar puntos en el campeonato mundial. Los puntos se distribuyen en función del lugar que el piloto termine en cada carrera.

Existen dos campeonatos principales en la Fórmula 1: el **Campeonato de Pilotos** y el **Campeonato de Constructores**. El primero premia al mejor piloto del año, mientras que el segundo premia al equipo con el mejor rendimiento general.
""")

# Mostrar una imagen de un coche de Fórmula 1 (archivo local)
st.subheader("Coche de Fórmula 1")
image_car = Image.open("imagecar.jpg")  # Asegúrate de tener esta imagen en el directorio
st.image(image_car, caption="Coche de Fórmula 1 en acción", width=700)

# Sección 3: Características de los coches de Fórmula 1
st.header("Características de los coches de Fórmula 1")
st.write("""
Los coches de Fórmula 1 son vehículos altamente especializados y diseñados específicamente para este tipo de competiciones. Algunas de las características más importantes incluyen:

- **Motor**: Los motores de los coches de F1 son extremadamente potentes, con una cilindrada de 1.6L V6 híbrido, lo que les permite alcanzar velocidades superiores a los 300 km/h.
- **Aerodinámica**: Los coches están diseñados para maximizar el agarre en la pista, utilizando alas y elementos aerodinámicos para reducir la resistencia del aire y mejorar la estabilidad a altas velocidades.
- **Neumáticos**: Los neumáticos son una parte clave de la competencia. Existen diferentes tipos de neumáticos según las condiciones climáticas, como neumáticos lisos para clima seco y neumáticos de lluvia para condiciones húmedas.
""")

# Mostrar una imagen de un pit stop (archivo local)
st.subheader("Pit Stop en Fórmula 1")
image_pit_stop = Image.open("imagenparadapits.jpg")  # Asegúrate de tener esta imagen en el directorio
st.image(image_pit_stop, caption="Pit stop en una carrera de Fórmula 1", width=700)

# Sección 4: ¿Cómo se gana una carrera?
st.header("¿Cómo se gana una carrera?")
st.write("""
Para ganar una carrera en la Fórmula 1, los pilotos deben completar el número de vueltas del circuito en el menor tiempo posible. Sin embargo, hay muchos factores que influyen en el resultado final:

- **Estrategia de carrera**: La elección de la estrategia de neumáticos es crucial. Los equipos deben decidir cuándo es el mejor momento para cambiar de neumáticos, basándose en el desgaste de los mismos y las condiciones de la pista.
- **Tiempo en los pit stops**: Los **pit stops** son momentos en los que el coche entra en boxes para cambiar neumáticos o realizar reparaciones rápidas. Los equipos de Fórmula 1 entrenan arduamente para hacer estos cambios lo más rápidos posibles.
- **Condiciones climáticas**: La lluvia, el calor o el viento pueden afectar la forma en que los pilotos compiten, lo que hace que la Fórmula 1 sea una disciplina impredecible.
""")

