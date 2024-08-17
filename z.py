from zanigma import ZANIGMA

rotor1 = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ","Q"]
rotor2 = ["AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"]  
rotor3 = ["BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"]  
reflector = "YXWVUTSRQPONMLKJIHGFEDCBAZ"
plugs = ['AC', 'BE']
settings = "AAA"
msg = "AAAAAAAAAAAAAAAAAAAAAAAAAA"
#msg = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
e = ZANIGMA(rotor3, rotor2, rotor1, reflector)
ctxt = e.input(msg, settings)
print(ctxt)
d = ZANIGMA(rotor3, rotor2, rotor1, reflector)
ptxt = d.input(ctxt, settings)
print(ptxt)
