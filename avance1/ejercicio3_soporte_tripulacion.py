# ============================================================
# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Grace Hernandez Guevara
# Fecha: 14/10/2026     Versión: 1.0
# Descripción: Verifica si la nave posee oxígeno y provisiones
#              suficientes para sostener a toda la tripulación.
# ============================================================

# --- Entrada de datos ---
oxigeno_disponible = int(input("Oxígeno disponible: "))
oxigeno_requerido = int(input("Oxígeno requerido: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))
provisiones_requeridas = int(input("Provisiones requeridas: "))

# --- Decisión y salida de resultados ---
# Se usa "and" porque el soporte solo es adecuado si AMBOS recursos alcanzan;
# se usa ">=" porque tener exactamente la cantidad requerida es suficiente.
# No se indica cuál recurso falla, tal como lo pide la consigna.
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")
