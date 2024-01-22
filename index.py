from tabulate import tabulate

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

                equipos_en_partido.append([local, gol_local])
                equipos_en_partido.append([visitante, gol_visitante])

                # TODO: Validar la existencia de los equipos en la tabla de posiciones
                # Obtener el nombre de los equipos
                equiposExistentes = []
                for equipo in range(len(tablaEquipos)):
                    equiposExistentes.append(tablaEquipos[equipo][0])

                # validar existencia de los equipos en partido en la tabla general de los equipos
                for equipo in range(len(equipos_en_partido)):
                    if equipos_en_partido[equipo][0] not in equiposExistentes:
                        print(True)
                        # cree al equipo con valores iniciales
                        tablaEquipos.append([equipos_en_partido[equipo][0], 0, 0, 0, 0, 0, 0, 0])

                # actulización de puntos en caso de existencia de alguno de los equipos
                for equipo in range(len(tablaEquipos)):
                    if gol_local > gol_visitante:
                        if tablaEquipos[equipo][0] == local:
                            tablaEquipos[equipo][1] += 1
                            tablaEquipos[equipo][2] += 1
                            tablaEquipos[equipo][5] += gol_local
                            tablaEquipos[equipo][6] += gol_visitante
                            tablaEquipos[equipo][7] += 3
                        if tablaEquipos[equipo][0] == visitante:
                            tablaEquipos[equipo][1] += 1
                            tablaEquipos[equipo][3] += 1
                            tablaEquipos[equipo][5] += gol_visitante
                            tablaEquipos[equipo][6] += gol_local
                    elif gol_local < gol_visitante:
                        if tablaEquipos[equipo][0] == local:
                            tablaEquipos[equipo][1] += 1
                            tablaEquipos[equipo][3] += 1
                            tablaEquipos[equipo][5] += gol_local
                            tablaEquipos[equipo][6] += gol_visitante
                        if tablaEquipos[equipo][0] == visitante:
                            tablaEquipos[equipo][1] += 1
                            tablaEquipos[equipo][2] += 1
                            tablaEquipos[equipo][5] += gol_visitante
                            tablaEquipos[equipo][6] += gol_local
                            tablaEquipos[equipo][7] += 3
                    else:
                        if tablaEquipos[equipo][0] == local:
                            tablaEquipos[equipo][1] += 1
                            tablaEquipos[equipo][4] += 1
                            tablaEquipos[equipo][5] += gol_local
                            tablaEquipos[equipo][6] += gol_visitante
                            tablaEquipos[equipo][7] += 1
                        if tablaEquipos[equipo][0] == visitante:
                            tablaEquipos[equipo][1] += 1
                            tablaEquipos[equipo][4] += 1
                            tablaEquipos[equipo][5] += gol_visitante
                            tablaEquipos[equipo][6] += gol_local
                            tablaEquipos[equipo][7] += 1

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
        print(tabulate(tablaEquipos))

    elif opcion == 2:
        print(tabulate(tablaEquipos))
        pass
    elif opcion == 3:
        pass
    else:
        pass



if __name__ == '__main__':
    main()