import pandas as pd
import matplotlib.pyplot as plt
import practica1_v2_Functions as p

dfinput = p.readFile("finanzas2020.csv", "\t")
if isinstance(dfinput, pd.DataFrame):
    df_gastos = p.getgastos(dfinput)
    df_ingresos = p.getingresos(dfinput)
    df_ahorro = p.getahorro(df_ingresos, df_gastos)

    print("¿Qué mes se ha gastado más?: " + p.maximogastos(df_gastos))
    print("¿Qué mes se ha ahorrado más?: " + p.maximoahorros(df_ahorro))
    print("¿Cuál es la media de gastos al año?: "
          + str(p.mediagastos(df_gastos)))
    print("¿Cuál ha sido el gasto total a lo largo del año?: "
          + str(p.sumtotal(df_gastos)))
    print("¿Cuáles han sido los ingresos totales a lo largo del año?: "
          + str(p.sumtotal(df_ingresos)))

    dfresult = pd.DataFrame({'MES': dfinput.columns.values,
                             'GASTOS': df_gastos.values,
                             'INGRESOS': df_ingresos.values})
    dfresult.plot(kind='line', x="MES", y="INGRESOS", color='red')
    plt.show()
