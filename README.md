# Misión Órbita

Simulador básico de exploración espacial en Python, desarrollado de forma progresiva para el curso **SOFT-01 Principios de programación 1** (Universidad CENFOTEC, sección SCV6, periodo C3-2026). Docente facilitadora: Verónica Mora Lezcano.

Este repositorio contiene el **Avance 1: Preparación de la misión**, formado por cuatro programas independientes que siguen el esquema entrada, procesamiento, decisión y salida.

## Integrantes

- Grace Hernandez Guevara (trabajo individual)

## Estructura del repositorio

```
mision-orbita/
├── README.md
├── avance1/
│   ├── ejercicio1_recursos.py
│   ├── ejercicio2_combustible.py
│   ├── ejercicio3_soporte_tripulacion.py
│   └── ejercicio4_autorizacion.py
└── documentacion/
    └── avance1.pdf
```

## Programas del Avance 1

| Archivo | Descripción | Estructura de control |
|---|---|---|
| `ejercicio1_recursos.py` | Calcula combustible (ida, regreso, reserva y total), oxígeno, energía y provisiones de una misión | Secuencial |
| `ejercicio2_combustible.py` | Verifica el combustible y advierte si el margen adicional es menor que 10 unidades | Condicional simple |
| `ejercicio3_soporte_tripulacion.py` | Verifica si el oxígeno y las provisiones alcanzan para la tripulación | Condicional doble (if/else) |
| `ejercicio4_autorizacion.py` | Autoriza o rechaza el lanzamiento evaluando los cuatro recursos | Condicional doble sin anidación |

Regla general de la misión: no basta con tener combustible para llegar al destino, también debe alcanzar para el regreso y la reserva de emergencia.

## Instrucciones para ejecutar

Requisitos: Python 3 instalado. No se necesitan librerías externas.

1. Clonar el repositorio y abrir una terminal en la carpeta `avance1`.
2. Ejecutar cada programa por separado:

```
python ejercicio1_recursos.py
python ejercicio2_combustible.py
python ejercicio3_soporte_tripulacion.py
python ejercicio4_autorizacion.py
```

3. Ingresar por consola los datos que solicita cada programa. Todos los valores son números enteros positivos, en unidades ficticias de misión.

## Convenciones y estilos

- **Nombres de variables:** descriptivos, en minúscula y notación `snake_case`.
- **Constantes:** en MAYÚSCULAS con guion bajo, declaradas al inicio del archivo (por ejemplo, `RESERVA_COMBUSTIBLE = 10`). No se usan números mágicos dentro de las fórmulas.
- **Formato:** indentación de 4 espacios, espacios alrededor de los operadores y líneas en blanco para separar bloques lógicos.
- **Mensajes de consola:** claros, con las unidades correspondientes.
- **Documentación:** cada archivo inicia con un encabezado (archivo, curso, integrantes, fecha, versión y descripción) y cada bloque lógico tiene un comentario que explica su propósito y el porqué de las decisiones.
- **Restricciones técnicas del avance:** sin ciclos, listas, tuplas, diccionarios, funciones propias, librerías, archivos, programación orientada a objetos ni condicionales anidadas o `elif`. Solo entrada y salida por consola.
- **Commits:** mensajes que describen la modificación realizada, por ejemplo: "Agrega validación de combustible de regreso en ejercicio 4".

## Documentación

El documento `documentacion/avance1.pdf` incluye, para cada ejercicio, la tabla de variables, el diagrama de flujo, el código, la tabla de casos de prueba y la evidencia de ejecución.
