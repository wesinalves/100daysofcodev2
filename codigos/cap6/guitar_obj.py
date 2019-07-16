from guitar import Guitar

g = Guitar()
print(g._brand, g._body)
print(g.play("strumming","98","Eu sou calebe"))

g.checkStrings()
g.tuneStrings()
g.checkStrings()
g.tuneStrings(['D','A','D','G','A','d'])
g.checkStrings()