def ejemplo(*args):
    for dato in args:
        print(dato)

ejemplo(1,2,3,"Salvador",[2,3,"Vernis"])

def nombre(**kwargs):#Por nombre
        print(kwargs)

nombre(a=(1,2,3),b=("Salvador"),c=[2,3,"Vernis"])

def nombre_posicion(*args, **kwargs):#Por nombre
        print(args, kwargs)

nombre_posicion(2,4,n=4)