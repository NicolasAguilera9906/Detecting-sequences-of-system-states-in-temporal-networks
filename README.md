# Escuela Colombiana de Ingeniería Julio Garavito

## Detecting sequences of system states in temporal networks

El siguiente proyecto tiene por objetivo poner en práctica los conocimientos adquiridos durante el curso Network science and machine learning on graphs en un problema real. Así, se trabajará en base al siguiente artículo: [Paper](https://www.nature.com/articles/s41598-018-37534-2.pdf) y los siguientes puntos serán tratados :

1. Introducción
2. Análisis de las redes presentadas en el texto.
3. Problema y método de solución propuesto por los autores.
4. Reproducción (parcial) de los experimentos presentados en el texto.
5. Resultados y análisis de los mismos
6. Conclusiones

## Introducción

Las interacciones entre sistemas normalmente dejan trazos entre ellos. Estas interacciones forman redes temporales que reflejan el estado de los sistemas. Así, en el paper se propone un método para asignar estados discretos a los sistemas e inferir la secuencia de esos estados de los datos.
Cada estado puede corresponder por ejemplo : a un estado mental, o a un estado operacional de una organización.

Este método combina medida de la distancia de un grafo y clustering jerárquico.
En este caso se emplea para inferir los diferentes estados dentro de un colegio en un dia entre semana y un fin de semana.

## Análisis de las redes presentadas en el texto

### Tipo de red

Estaremos trabajando sobre una red social. Dentro de esta red, cada uno de los nodos corresponderá a un estudiante o un profesor. Además, la conexión entre ellos representará su comunicación durante algún momento del día dentro del colegio.

### Estructura de la red

Se trabajará todo el tiempo sobre redes reales. En este sentido, son redes particularmente asortativas, en donde los estudiantes que pertenezcan a la misma clase o estén en el mismo grado escolar estarán más propensos a crear vinculos entre ellos.

Además, se tienen un par de consideraciones acerca del estado de una red:

1. El estado de la red será considerado como un todo, más que el comportamiento de nodos individuales.
2. El estado de la red está codificado en los bordes (es decir, interacciones por pares) y se puede resumir como una serie temporal de cambios de estado.

## Problema y método de solución propuesto.

### Problema

Es sencillo, para redes estáticas en el tiempo, obtener información condensada sobre las interacciones que ocurren dentro de ella. Este objetivo es conseguido por medio de la detección de comunidades que nos permite encontrar particiones de la red en grupos fuertemente conectados dentro de cada uno, pero debilmente conectados entre ellos. Sin embargo, muchas redes en el mundo real están cambiando con el tiempo. En ese sentido, la teoría tradicional de redes para redes estáticas no aplica. Así, se hace necesario un estudio sobre las redes temporales, en la cual los nodos y conexiones están marcados con el tiempo.

Por ejemplo, el comportamiento humano puede ser modelado como una secuencia de estados discretos entre el cuál el sistema estocásticamente cambia. De esta manera, el comportamiento humano al recibir un email puede ser modelado como un proceso de dos puntos de estado, en el cuál el individuo es asumido entre un estado activo y un estado normal.

### Solución

El objetivo será distinguir entre estados discretos de redes temporales y demostrar que estos estados son interpretables.






