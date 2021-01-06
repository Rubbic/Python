try:
    n = None
    
    if n is None:
        raise ValueError("Error! No se permite un valor nulo")
except ValueError:
    print("No se permite un valor nulo")