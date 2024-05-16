import sys

def PreguntarDeNuevo():  #Funcion para preguntar de nuevo
    while True:
        try:
            reiniciarL = str(input("Desea realizar otra liquidación S/N: "))
            reiniciarL = reiniciarL.upper()
            if reiniciarL == "S" or reiniciarL == "N":
                return reiniciarL
            else:
                print("Error, ingrese S/N")
        except ValueError:
            print("Error, ingrese S/N")

while True:
    while True:
        try:
            nombreUsuario = input("Ingrese su nombre: ").strip() # para que no se deje el nombre sin responder
            if nombreUsuario and len(nombreUsuario) <= 30: # maximo 30 letras
                break
            else:
                print("El nombre no puede estar vacío y no debe contener más de 30 letras")
        except ValueError:
            print("Error, ingrese un nombre válido")

    while True:
        try:
            sueldoBase = float(input("Ingrese su sueldo: "))  
            if sueldoBase > 0:
                break
            else:
                print("El sueldo debe ser un valor numérico positivo") 
        except ValueError:
            print("El sueldo debe ser un valor numérico")    # para verificar que sea un valor numerico positivo

    while True:
        try:
            horasTrabajadas = float(input("Ingrese horas trabajadas: "))
            if horasTrabajadas <= 180:
                print("Horas trabajadas:", horasTrabajadas)
                break
            else:
                horasExtras = horasTrabajadas - 180
                pagoPorHora = (sueldoBase / 180) * 1.5  #horas extra solucion
                pagoExtras = horasExtras * pagoPorHora
                print("Horas extras:", horasExtras)
                pagoExtraR = int(round(pagoExtras))
                print("Pago por horas extras:", pagoExtraR)
                break
        except ValueError:
            print("Debe ingresar un valor numérico positivo para las horas trabajadas")

    ingresoTotal = sueldoBase + horasExtras
    DesFonasa = sueldoBase * 0.07
    desAfP = sueldoBase * 0.1
    DescuentoSeguridad = DesFonasa + desAfP
    SueldoNeto = sueldoBase - DescuentoSeguridad

    def DesgloseDeLiquidacion(nombreUsuario, sueldoBase, horasExtras, ingresoTotal, descuentoSeguridad, SueldoNeto): #Crear una funcion para el desglose de liquidacion
        print("---- Liquidación De Sueldo ---- ")
        print("Nombre del trabajador:", nombreUsuario)
        print("Total horas Extra:", horasExtras)
        print("Ingreso total:", ingresoTotal)
        print("Descuento por seguridad social:", descuentoSeguridad)
        print("Sueldo Neto:", SueldoNeto)

    DesgloseDeLiquidacion(nombreUsuario, sueldoBase, horasExtras, ingresoTotal, DescuentoSeguridad, SueldoNeto) 

    with open(f"Liquidacion_{nombreUsuario}.txt", "w", encoding="utf-8") as archivo:
        archivo.write("---- Liquidación De Sueldo ----\n")
        archivo.write(f"Nombre: {nombreUsuario} \t\t Sueldo base: {sueldoBase}\n")
        archivo.write(f"Horas extras a pagar: {horasExtras} \t\t Ingreso total: {ingresoTotal}\n")
        archivo.write(f"Descuento por seguridad social: {DescuentoSeguridad} \t\t Sueldo Neto: {SueldoNeto}\n")

    reiniciarL = PreguntarDeNuevo()
    if reiniciarL == "N":
        print("Hasta luego")
        sys.exit()
    else:
        print("Intente de nuevo")
