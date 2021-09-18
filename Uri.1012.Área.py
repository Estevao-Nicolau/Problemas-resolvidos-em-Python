a,b,c = input().split()

a = float(a)
b = float(b)
c = float(c)

triangulo = (a * c)/2
raio =  3.14159 * c**2
area_trapezio = c * ( a + b) / 2
area_quadrado = b * b     
area_retangulo = a * b 

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {raio:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')
