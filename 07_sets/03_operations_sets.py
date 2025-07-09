# Conjuntos de ejemplo
matematicas = {"Alice", "Bob", "Charlie", "David"}
informatica = {"Charlie", "David", "Eve", "Frank"}
musica = {"Alice", "Frank", "Grace"}

print(f"Estudiantes de Matemáticas: {matematicas}")
print(f"Estudiantes de Informática: {informatica}")
print(f"Estudiantes de Música: {musica}")

# Unión (union |)
# Estudiantes en Matemáticas O Informática
todos_estudiantes = matematicas.union(informatica)
print(f"\nUnión (Matemáticas | Informática): {todos_estudiantes}")
# También con el operador: matematicas | informatica | musica

# Intersección (intersection &)
# Estudiantes en Matemáticas Y Informática
comunes_mat_inf = matematicas.intersection(informatica)
print(f"Intersección (Matemáticas & Informática): {comunes_mat_inf}")

# Estudiantes en las tres materias
comunes_tres = matematicas.intersection(informatica, musica)
print(f"Intersección (Matemáticas & Informática & Música): {comunes_tres}")

# Diferencia (difference -)
# Estudiantes en Matemáticas pero NO en Informática
solo_matematicas = matematicas.difference(informatica)
print(f"Diferencia (Matemáticas - Informática): {solo_matematicas}")

# Estudiantes en Informática pero NO en Matemáticas
solo_informatica = informatica - matematicas
print(f"Diferencia (Informática - Matemáticas): {solo_informatica}")

# Diferencia simétrica (symmetric_difference ^)
# Estudiantes que están en uno de los cursos (Matemáticas O Informática), pero NO en ambos
exclusivos_mat_inf = matematicas.symmetric_difference(informatica)
print(f"Diferencia Simétrica (Matemáticas ^ Informática): {exclusivos_mat_inf}")

# Subconjuntos y Superconjuntos
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 6}

print(f"\n¿A es subconjunto de B? {A.issubset(B)}")   # Salida: True (todos los elementos de A están en B)
print(f"¿B es superconjunto de A? {B.issuperset(A)}") # Salida: True (todos los elementos de A están en B)
print(f"¿A es subconjunto de C? {A.issubset(C)}")   # Salida: False