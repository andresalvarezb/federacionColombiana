def main():
    # CREACION DE EQUIPOS
    # LECTURA DE EQUIPOS (TABLA DE POSICIONES)
    # ACTUALIZACIÓN DE EQUIPOS
    # ELIMINACINACIÓN DE EQUIPOS (SALIDA DEL PROGRAMA)

    print("""
    MENÚ
    1 - Registrar una fecha
    2 - Consultar tabla de posiciones
    3 - Salida del programa""")

    opcion = int(input('Opción: '))

    if opcion == 1:
        # Creación de fechas
        hayFecha = True
        fecha = 1
        while hayFecha:
            print(f'FECHA #{fecha}')

            # Creacion de partidos
            hayPartidos = True
            partido = 1
            while hayPartidos:
                print(f"""
                {'-'*9}
                PARIDO {partido}
                {'-'*9}""")

                # registro por partido
                equipos_en_partido = []
                local = input(f'Equipo local: ').lower()
                gol_local = int(input('Goles: '))
                visitante = input(f'Equipo visitante: ').lower()
                gol_visitante = int(input('Goles: '))

                # TODO: Validar la existencia de los equipos en la tabla de posiciones

            agregarFecha = input('Agregar otra fecha [Y/N]: ')
            if agregarFecha.lower() == 'y':
                hayFecha = True
            else:
                hayFecha = False

    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    else:
        pass


if __name__ == '__main__':
    main()