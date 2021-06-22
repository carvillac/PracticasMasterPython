import pandas as pd
import matplotlib.pyplot as plt


class Error(Exception):
    pass


class NumeroColumnasError(Error):
    pass


class NoTieneContenido(Error):
    pass


def getgastos(df):
    return df.apply(lambda x: x[x < 0].sum(), axis=0)


def getingresos(df):
    return df.apply(lambda x: x[x > 0].sum(), axis=0)


def getahorro(df_ingresos, df_gastos):
    return {key: df_ingresos[key] + df_gastos.get(key, 0)
            for key in df_ingresos.keys()}


def maximogastos(df_gastos):
    return df_gastos.idxmin()


def maximoahorros(df_ahorro):
    return max(df_ahorro, key=df_ahorro.get)


def mediagastos(df_gastos):
    return round(df_gastos.mean(), 2)


def gastostotal(df_gastos):
    return df_gastos.sum()


def ingresostotales(df_ingresos):
    return df_ingresos.sum()


def readFile(name, delimi):

    try:
        dfinput = pd.read_csv(name, delimiter=delimi)

        row, col = dfinput.shape
        if(col != 12):
            raise NumeroColumnasError

        df_count = dfinput.count()
        if (df_count.eq(0).any()):
            raise NoTieneContenido

    except FileNotFoundError:
        print("Archivo no encontrado o erroneo")
    except NumeroColumnasError:
        print("El número de columnas es incorrecto")
    except NoTieneContenido:
        print("Existe alguna columna sin contenido")
    else:
        dfinput = dfinput.replace("'", "", regex=True)
        dfinput = dfinput.apply(pd.to_numeric, errors='coerce').fillna(0)

    return dfinput


try:
    dfinput = readFile("finanzas2020.csv", "\t")
except (FileNotFoundError, NumeroColumnasError, NoTieneContenido):
    print("No se puede procesar el fichero")
else:
    df_gastos = getgastos(dfinput)
    df_ingresos = getingresos(dfinput)
    df_ahorro = getahorro(df_ingresos, df_gastos)

    print("¿Qué mes se ha gastado más?: " + maximogastos(df_gastos))
    print("¿Qué mes se ha ahorrado más?: " + maximoahorros(df_ahorro))
    print("¿Cuál es la media de gastos al año?: " + str(mediagastos(df_gastos)))
    print("¿Cuál ha sido el gasto total a lo largo del año?: " + str(gastostotal(df_gastos)))
    print("¿Cuáles han sido los ingresos totales a lo largo del año?: " + str(ingresostotales(df_ingresos)))

    dfresult = pd.DataFrame({'MES': dfinput.columns.values,
                             'GASTOS': df_gastos.values,
                             'INGRESOS': df_ingresos.values})
    dfresult.plot(kind='line', x="MES", y="INGRESOS", color='red')
    plt.show()
