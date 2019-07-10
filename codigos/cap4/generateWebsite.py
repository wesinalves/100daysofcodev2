def generateWebsite(name, url="www.meusite.com", 
    flash ="no", django="yes"):

    print("Gerando um website para:", name, "usando a url:", url)

    if flash == "yes":
        print("com Flash habilitado")
    if django == "yes":
        print("desenvolvido com framework django")
    
    print("\n")

generateWebsite("João")
generateWebsite("João", flash="yes", url="www.joao.com")
generateWebsite(django="no", name="Pedro")


