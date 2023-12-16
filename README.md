Cuestionario de Monitoreo

#### Explica los resultados obtenidos además de los métodos para detectar anomalías (debes explicarlo NO solo mencionarlo)

Ricardo: En este ejercicio, el algoritmo Isolation Forest mostró ligeramente una mejor identificación de anomalías vs SVM One-Class. Sin embargo esto no es necesariamente una generalización de mejor rendimiento de un algoritmo sobre otro, ya que intervienen tanto la hiperparametrización como los supuestos de distribución de datos en  cada algoritmo y la distribución de las anomalías. En el caso particular de % de anomalías esperadas, en ambos modelos se estableció un 10%: nu = 0.1 y contamination = 0.1 para SVM e Isolation Forest respectivamente.
