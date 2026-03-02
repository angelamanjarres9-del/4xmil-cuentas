#promed
print("bienvenido estudiante UniAtlanticente, a continuacion se calculara la nota final de tu semestre")
nota_primer_corte = float(input ("Nota primer corte(30%): "))
nota_segundo_corte = float(input("Nota segundo corte(30%): "))
nota_tercer_corte = float (input ("Nota tercer corte(40%): "))
 

nota_final = (nota_primer_corte * 0.30 +
nota_segundo_corte * 0.30 + nota_tercer_corte * 0.40 )

print (f"tu nota final es {nota_final}")