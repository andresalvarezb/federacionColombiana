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

    tablaEquipos = []

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

                equipos_en_partido.append([local, visitante])

                # TODO: Validar la existencia de los equipos en la tabla de posiciones
                # Obtener el nombre de los equipos
                equiposExistentes = []
                for equipo in range(len(tablaEquipos)):
                    equiposExistentes.append(tablaEquipos[equipo][0])

                # validar existencia de los equipos en partido en la tabla general de los equipos
                for equipo in range(len(equipos_en_partido)):
                    if equipos_en_partido[equipo] in equiposExistentes:
                        # actualice datos
                        pass
                    else:
                        # cree al equipo con valores iniciales segun marcador
                        if gol_local > gol_visitante:
                            tablaEquipos.append([local, 1, 1, 0, 0, gol_local, gol_visitante, 3])
                            tablaEquipos.append([visitante, 1, 0, 1, 0, gol_visitante, gol_local, 0])
                        elif gol_local < gol_visitante:
                            tablaEquipos.append([local, 1, 0, 1, 0, gol_local, gol_visitante, 0])
                            tablaEquipos.append([visitante, 1, 1, 0, 0, gol_visitante, gol_local, 3])
                        else:
                            tablaEquipos.append([local, 1, 0, 0, 1, gol_local, gol_visitante, 1])
                            tablaEquipos.append([visitante, 1, 0, 0, 1, gol_visitante, gol_local, 1])

                agregarPartido = input('Agregar otro partido [Y/N]: ')
                if agregarPartido.lower() == 'y':
                    hayPartidos = True
                    partido += 1
                else:
                    hayPartidos = False







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

    print(tablaEquipos)


if __name__ == '__main__':
    main()