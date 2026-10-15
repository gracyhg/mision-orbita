# ============================================================
# Archivo: ejercicio4_autorizacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Nombre Apellido 1, Nombre Apellido 2, Nombre Apellido 3
# Fecha: dd/10/2026     Versión: 1.0
# Descripción: Autoriza o rechaza el lanzamiento de una misión
#              según el combustible, oxígeno, energía y provisiones.
# ============================================================

# --- Declaración de constantes ---
# Se declara al inicio para evitar números mágicos en las fórmulas.
RESERVA_COMBUSTIBLE = 10

# --- Entrada de datos ---
combustible_disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para llegar al destino: "))
combustible_regreso = int(input("Combustible requerido para regresar: "))
oxigeno_disponible = int(input("Oxígeno disponible: "))
oxigeno_requerido = int(input("Oxígeno requerido: "))
energia_disponible = int(input("Energía disponible: "))
energia_requerida = int(input("Energía requerida: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))
provisiones_requeridas = int(input("Provisiones requeridas: "))

# --- Procesamiento ---
# El combustible se compara contra el total (ida + regreso + reserva), no solo
# contra la ida: una nave que únicamente puede llegar quedaría varada.
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# --- Decisión y salida de resultados ---
# Una sola condición compuesta con "and": si falla cualquier recurso se rechaza.
# Se usa ">=" porque contar exactamente con lo requerido es suficiente.
# No se indica cuál recurso causó el rechazo, tal como lo pide la consigna.
if (combustible_disponible >= combustible_total
        and oxigeno_disponible >= oxigeno_requerido
        and energia_disponible >= energia_requerida
        and provisiones_disponibles >= provisiones_requeridas):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")
