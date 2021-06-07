frase = '     Curso em vídeo Python     '

print(frase)
print(frase[4])
print(frase[1:15:2])
print(frase[::2])

print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, ' \
when an unknown printer took a galley of type and scrambled it to make a type
specimen book. It has survived not only five centuries, but also the leap into
electronic typesetting, remaining essentially unchanged. It was popularised in
the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
and more recently with desktop publishing software like Aldus PageMaker
including versions of Lorem Ipsum.""")

print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.strip())
print(frase.replace('Python', 'Android'))

print('*'*50)
print(frase, '\n')
frase = frase.strip().replace('Python', 'Android')
print(frase, '\n')
print(frase.split(), '\n')

print('*' * 50)
dividido = frase.split()
print(dividido[2][3]) # pegar o dividido na posição 2, e pegar a letra na posição 3

