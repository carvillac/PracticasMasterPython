import pandas as pd
import matplotlib.pyplot as plt


class Error(Exception):
    pass


class NumeroColumnasError(Error):
    pass


class NoTieneContenido(Error):
    pass


try:
    dfinput = pd.read_csv("finanzas2020.csv", delimiter="\t")

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

    df_gastos = dfinput.apply(lambda x: x[x < 0].sum(), axis=0)
    df_ingresos = dfinput.apply(lambda x: x[x > 0].sum(), axis=0)
    df_ahorro = {key: df_ingresos[key] + df_gastos.get(key, 0)
                 for key in df_ingresos.keys()}

    print("¿Qué mes se ha gastado más?: " + df_gastos.idxmin())
    print("¿Qué mes se ha ahorrado más?: " + max(df_ahorro, key=df_ahorro.get))
    print("¿Cuál es la media de gastos al año?: " + str(round(df_gastos.mean(), 2)))
    print("¿Cuál ha sido el gasto total a lo largo del año?: " + str(df_gastos.sum()))
    print("¿Cuáles han sido los ingresos totales a lo largo del año?: " + str(df_ingresos.sum()))

    dfresult = pd.DataFrame({'MES': dfinput.columns.values,
                             'GASTOS': df_gastos.values,
                             'INGRESOS': df_ingresos.values})
    dfresult.plot(kind='line', x="MES", y="INGRESOS", color='red')
    plt.show()
