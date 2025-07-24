from utils import *

def main():
    
    glicose = int_min("Glicose: ",0)
    classificar_diabetes = classificar(glicose)
    print(classificar_diabetes)
    
def classificar(glicose):
    
    if glicose < 100:
        return 'Normal'
    elif 100 <= glicose <= 125:
        return 'Pré-Diabetes'
    else:
        return 'Diabetes'

    
    
main()