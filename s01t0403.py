'''
NOTAS:
1.⁠ ⁠Identifco el tamaño de la entrada "n"
El tamaño de la entrada es el numero
de estudiantes.
2.⁠ ⁠Es ver cuanto crece el numero de
operaciones en mi algoritmo conforme
creece el tamaño de la entrada
Agrego las bigO identicadas
Teniendo en cuenta la Cota superior asintotica
O(n) + O(4) = O(n+4) = O(n)
'''

# Creando las listas de estudiantes 
students_list_01 = ['luis', 'fran', 'becerro', 'alvin']
students_list_02 = ['piglet', 'oscar', 'pipope', 'luz']

# Verificando la presencia de un estudiante 
def check_student(input_student, students_list):
    for student in students_list:
        if input_student == student:
            print("Estudiante encontrado")
            return student
            
    # El caso "no encontrado" va fuera del bucle for
    print("❌Estudiante no encontrado") #0(1)
    return None

# Probando el algoritmo 
check_student('kevin', students_list_01)

