#https://www.codewars.com/kata/57b58827d2a31c57720012e8

def fuel_price(litres, price_per_litre):
    if litres > 10:
        return (litres * (price_per_litre - 0.25))
        # Como a partir de 10 litros el precio es fijo, devolvemos la operación por return inmediatamente con el descuento fijo aplicado.
    else:
        return round((litres * (price_per_litre - litres // 2 * 0.05)), 2)
        # Como el descuento depende de la cantidad de litros en múltiplos de 2, le hacemos una división floor y lo multiplicamos por el incremento de descuento.
        # En los Random Test puede volverse un poco loco con los decimales, por lo que antes de la operación utilizamos round() para asegurarnos de que cumplimos el enunciado.
