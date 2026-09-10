import sys

def main():
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        result = num1 + num2
        print(f'La suma es: {result}')
    except ValueError:
        print('Error: Por favor ingrese números válidos.')

if __name__ == '__main__':
    if len(sys.argv)!= 3:
        print('Uso: python main.py <num1> <num2>')
    else:
        main()