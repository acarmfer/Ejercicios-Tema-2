texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

# Reemplazar "#" por "\n\n- "
texto_transformado = texto.replace("#", "\n\n- ")

# Capitalizar la primera letra del texto
texto_transformado = texto_transformado.capitalize()

print(texto_transformado)