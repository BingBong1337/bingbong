def victor():
    victor == input('Vad är victor?')
    return victor

def gay():
    gay == gay
    return gay



def main():
    operator = ''
    while operator != 'q':
        operator = input("""vad är victor? (q avslutar) (gay)""")
        if operator == 'gay':
            victor = gay()
            print('Victor Är Gay')
        elif operator == 'q':
            print('victor är gay')
            break
        else:
            print('ok')
main()
