dict = {
    {"""nombre:  Facundo,
     telefono: 123456789,
     email: facundo@gmail.com
     direccion: Calle Falsa 123"""
     },
    {"""nombre:  Maria,
        telefono: 987654321,
        email: maria@gmail.edu
        direccion: Avenida Siempre Viva 742"""
     },
    {"""nombre:  Juan,
        telefono: 456123789,
        email: juan@gmail.edu
        direccion: Calle Luna 456"""
    }
}


print(f'''--- Agenda de Contactos: Facundo---
    telefono: {dict.get('facundo').get('telefono')}
    email: {dict.get('facundo').get('email')}
    direccion: {dict.get('facundo').get('direccion')}
''')


dict['Fabian'] = {"""
    telefono : 3385590014
    email : fabian@gmial.com
    direccion : Calle Sol 321"""   
    }

print(f"Se agrego a fabian{dict}. ")

dict.pop('Juan')
print(f"Se borro a juan {dict}")