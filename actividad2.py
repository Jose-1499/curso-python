# pueblos = ["Bogotá","Medelliin", "Cali","Pereira"]

# pueblos.append("Tolima")

# pueblos.remove("Cali")

# pueblos.sort()

# print(pueblos)

# nombre = (input("Ingrese su nombre: "))
# edad = int(input("Ingrese su edad: "))
# ciudad = (input("Ingrese su ciudad de nacimiento: "))
# profesion = (input("Ingrese su profesión: "))

# persona = { 
#     "nombre":nombre,
#     "edad": edad,
#     "ciudad": ciudad,
#     "profesion": profesion
# }

# print(f"""Información ingresada: 
#       Nombre:{persona['nombre']}
#       Edad: {persona['edad']}
#       Ciudad: {persona['ciudad']}
#       Profesión: {persona['profesion']}""")

# nueva_ciudad = input("Ingresa la nueva ciudad para actualizar: ")
# persona["ciudad"] = nueva_ciudad

# # 5. Agregar teléfono
# telefono = input("Ingresa un número de teléfono: ")
# persona["telefono"] = telefono

# # 6. Mostrar solo claves
# print("Claves del diccionario:")
# print(persona.keys())

# # 7. Mostrar solo valores
# print("Valores del diccionario:")
# print(persona.values())

numeros = [1, 2, 3, 2, 4, 5, 1, 3, 6, 4]

# 2. Convertir la lista en un set (elimina duplicados)
numeros_unicos = set(numeros)

print(f"Elementos originales: {len(numeros)}")
print(f"Elementos únicos después de eliminar duplicados: {len(numeros_unicos)}")

# Mostrar el set si quieres ver el resultado
print("Set resultante:", numeros_unicos)