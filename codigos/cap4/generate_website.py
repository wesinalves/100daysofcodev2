'''
How to program in Python - Chapter 4
Named arguments examples
'''


def generate_website(name, url="www.meusite.com",
                     flash="no", django="yes"):
    '''Genereate url to website'''

    print("Gerando um website para:", name, "usando a url:", url)

    if flash == "yes":
        print("with Flash enabled")
    if django == "yes":
        print("developed wiht django framework")

    print("\n")


generate_website("João")
generate_website("João", flash="yes", url="www.joao.com")
generate_website(django="no", name="Pedro")
