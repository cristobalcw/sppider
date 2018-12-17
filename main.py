import os, os.path, time, sys
import hashlib, mmap
from pathlib import Path



#directorio en el que se va a trabajar pero se puede expandir a otros mas

dataPath = Path("E:/proyecto antivirus/descargas")
 
#prueba del algoritmo detector de nuevos archivos
path_to_watch = "E:/proyecto antivirus/descargas"
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  
    time.sleep (2)
    after = dict ([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    
#variable que contiene la ruta mas el archivo a abrir
    if added:
        filenameTwo = str("".join(added))
        print (filenameTwo)
        before = after
###############hasta aqui es el monitoreo del directorio######################

######obtener hash######
        

        path_to_open = path_to_watch + "/" + filenameTwo
        sha256_hash = hashlib.sha256()



        with open(path_to_open,"rb") as f:

        # Read and update hash string value in blocks of 4K

            for byte_block in iter(lambda: f.read(4096),b""):

                sha256_hash.update(byte_block)
                
                hashedWord = str(sha256_hash.hexdigest())
                print(hashedWord)
#############################################aqui termina la parte de monitoreo y obtener hash################################

#############################################busqueda de hash en archivo de definiciones#######################################
        
            with open("E:/proyecto antivirus/antivirus/base datos/definiciones_virus.txt") as search:
                for line in search:
                    line = line.rstrip()  # remove '\n' at end of line
                    if hashedWord == line:
                        print("El archivo es malicioso")
                    
            
                    
                
    

        
    


    

    
    



     
