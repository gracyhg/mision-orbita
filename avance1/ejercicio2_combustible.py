# ============================================================
# Archivo: ejercicio2_combustible.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Nombre Apellido 1, Nombre Apellido 2, Nombre Apellido 3
# Fecha: dd/10/2026     Versión: 1.0
# Descripción: Verifica si una nave posee suficiente combustible
#              y advierte cuando el margen adicional es bajo.
# ============================================================

# --- Declaración de constantes ---
# Se declaran al inicio para evitar números mágicos en las fórmulas.
RESERVA_COMBUSTIBLE = 10
MARGEN_MINIMO_ADVERTENCIA = 10

# --- Entrada de datos ---
combustible_disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para el viaje de ida: "))
combustible_regreso = int(input("Combustible requerido para el viaje de regreso: "))

# --- Procesamiento ---
# El total incluye el regreso y la reserva: no basta con llegar al destino.
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
combustible_adicional = combustible_disponible - combustible_total

# --- Salida de resultados ---
# Estas salidas se muestran siempre, sin importar el margen adicional.
print("Combustible disponible:", combustible_disponible, "unidades")
print("Combustible requerido para llegar:", combustible_ida, "unidades")
print("Combustible requerido para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Combustible adicional:", combustible_adicional, "unidades")

# --- Decisión ---
# Condicional simple: la advertencia solo aparece si el margen es menor que 10.
# Se usa "<" y no "<=" porque con exactamente 10 unidades el margen es aceptable.
if combustible_adicional < MARGEN_MINIMO_ADVERTENCIA:
    print("Advertencia: el margen adicional de combustible es bajo.")
