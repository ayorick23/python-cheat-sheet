def reverseString(text):
    #Devuelve la cadena al revés
    return text[::-1]

def countVowels(text):
    #Cuenta las vocales en una cadena"
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

if __name__ == "__main__":
    print(reverseString("Hola"))
    print(countVowels("Python es el mejor"))