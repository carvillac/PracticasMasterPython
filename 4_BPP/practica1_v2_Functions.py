import pandas as pd


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


def sumtotal(df_gastos):
    return df_gastos.sum()


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
        dfinput = ""
    except NumeroColumnasError:
        print("El número de columnas es incorrecto")
        dfinput = ""
    except NoTieneContenido:
        print("Existe alguna columna sin contenido")
        dfinput = ""
    else:
        dfinput = dfinput.replace("'", "", regex=True)
        dfinput = dfinput.apply(pd.to_numeric, errors='coerce').fillna(0)
    return dfinput
