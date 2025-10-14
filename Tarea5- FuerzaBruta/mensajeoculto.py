def descifrar_cesar(mensaje_cifrado):
    """Intenta descifrar el texto cifrado con el cifrado césar probando
    todas las claves posibles (buerza bruta)"""

    alfabeto = "abcdefghijklmnñopqrstuvwxyz ,."
    longitud_alfabeto= len(alfabeto)

    print("Alfabeto:", alfabeto)
    print("=" * 80)

    #reconoce cada símbolo en el texto cifrado
    for clave in range(longitud_alfabeto):
        texto_descifrado = ""

        for caracter in mensaje_cifrado:
            if caracter in alfabeto:
                pos_actual = alfabeto.index(caracter)
                pos_nueva = (pos_actual - clave) % longitud_alfabeto
                texto_descifrado += alfabeto[pos_nueva]
            else:
                texto_descifrado += caracter
                
        #imprime el resultado para el desplazamiento actual
        print(f"CLAVE {clave:2d}: {texto_descifrado}")
        print()

#el texto que se va a descifrar
texto_cifrado =  "l.ziu,mf .fzmk,wzilwgfqw mfai kwukmsw flw,wfifsif.upamz plilflmf .fik,.isfm k.lwfmufmsfk.isfmsfiñ.psiftmcpkiuifdfmsfkwulwzfiulpuwgfk.isfiamfjpkmnisigfxzw,mñmufmsflm xspmñ.mflmsftixiflmfitmzpkifsi,puigflm lmfsifnzwu,mzifuwz,mflmftmcpkwfoi ,ifmsfkijwflmfowzuw gfxsi tiulwfsif.upnpkikpwuflmfsw fpjmzwitmzpkiuw gfu.m ,zwfkwu,pumu,mfu.mawfdfiu,pñ.wgfxzmlm ,puilwfifkwu,mumzf.uifzieify.pu,igfsifzieifkw tpkigfmufsifk.isf mfn.ulpziufsi flp xmz i fdf mfkwu .tizifsif.uplilh"

descifrar_cesar(texto_cifrado)