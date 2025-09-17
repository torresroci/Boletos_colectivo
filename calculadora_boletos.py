print("CALCULADORA DE COLECTIVO")
numero_boletos = int(input("\n ingrese el numero de boletos:"))
precio_boleto = float(input("Precio por boleto: $"))
precio_total = numero_boletos * precio_boleto
print("=== TOTAL ===")
print(f"El total a pagar es: {precio_total} pesos")