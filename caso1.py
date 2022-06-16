"""rograma que por cada estudiante lea el código 
y las 5 notas del periodo de una materia, y que calcule e imprima el código y la nota final de cada estudiante"""

print("--------------------------------")
print("------ NOTAS ESTUDIANTES -------")
print("--------------------------------")

#Entrada 
cod = int(input("Digite el codigo del estudiante:  "))

if cod!= 0:
    nota1 = float(input("Digite la nota de la evaluación 1: "))
    nota2 = float(input("Digite la nota de la evaluación 2: "))
    nota3 = float(input("Digite la nota de la evaluación 3: "))
    nota4 = float(input("Digite la nota de la evaluación 4: "))
    nota5 = float(input("Digite la nota de la evaluacion 5. "))

else:
    print("Fin de la entrada")

#processing
reprobados = 0

while cod != 0:
    nota_final = (nota1 + nota2 + nota3 + nota4 + nota5)/5
    print("El estudiante de código " + str(cod) +  " tuvo una nota difinitiva de " + str(nota_final))
    if nota_final < 5:
        reprobados = reprobados + 1
    #Entrada 
    cod = int(input("Digite el codigo del estudiante: "))
    if cod!=0:
        nota1 = float(input("Digite la nota de la evaluación 1: "))
        nota2 = float(input("Digite la nota de la evaluación 2: "))
        nota3 = float(input("Digite la nota de la evaluación 3: "))
        nota4 = float(input("Digite la nota de la evaluación 4: "))
        nota5 = float(input("Digite la nota de la evaluación 5: "))
    else:
        print("Fin de la entrada ") 
#output
print("Cantidad de estudiantes que perdieron la asignatura: " + str(reprobados)) 
           
    
   
