# Cuestionario de Monitoreo

## Creación de un dashboard para monitorear modelo de Datos
Explica cada una de las métricas que ves en el dashboard y has una interpretación de las
mismas respecto a lo que ves en las gráficas
- Andres: En el dashboard se muestran tres métricas del desempeño de nuetro clasificador binario: precisión, recall y exactitud. Intuyendo que la principal métrica del negocio es la precisión se puede tratar de un problema donde se buscan reducir los falsos positivos por encima de lo que obtendriamos de maximizar el recall en donde reduciriamos los falsos negativos o en la exactitud donde solo nos interesan las predicciones correctas. Particularmente en este modelo notamos que el desempeño del mismo fluctuó a lo largo de la ventana de tiempo teniendo máximos locales tanto en la precisión como el recall el 2 y 8  de enero. Sin embargo el comportamiento del modelo fue distinto en ambas fechas ya que para el 2 de enero se tuvo una reducción en la exactitud a pesar del aumento en la precisión del mismo día lo que significa que las predicciones tienen baja variabilidad pero no fueron muy cercanas al valor real. Caso contrario a lo que ocurre el 8 de enero en el que tanto la precición como la exactitud subieron en ese día indicando que las predicciones fueron consistentes y cercanas al valor real. De manera general habría que considerar una ventana más grande de tiempo de monitorio y conocer el contexto del problema para poder interpretar de mejor manera el desempeño de este modelo. 

## Monitoreo de modelos
Compara las distancias obtenidas. 1.- ¿Cómo interpretarías estos
resultados? 2.-¿Qué implicaciones tiene para la similitud o diferencia
entre las distribuciones?
- Andrés: Al obtener unas distancia de 0 y 0.05 para las pruebas de Wassertein y Jensen-Shannon, respectivamente podemos interpretar que las distribuciones 1 y 2 son iguales, por lo tanto al ser iguales podemos suponer que no existe un data drift en los datos aún. 

## Detección de Anomalías con Isolation Forest y One-Class SVM
Explica los resultados obtenidos además de los métodos para detectar
anomalías (debes explicarlo NO solo mencionarlo)
- Andrés: Isolation-Forest funciona detectando anomalías realizando divisiones por cada característica identificando a las anomalías como las observaciones que requirieron más nodos de división. Por otro lado, 1-SVM funciona de manera similar a los métodos supervisados de SVM solo que en esta ocasión en lugar de encontrar un hiperplano que separe el espacio de características en las clases entregadas(target) se construye un hiperplano que esté lo más cercano a los puntos en el espacio posible. Las observaciones que queden fuera del hiperplano serán consideradas como anomalías. Al aplicar ambos métodos se notan diferencias en los resultados ya que ambos métodos identificaron como anomalías observaciones que no estaban definidas como tal, esto debido a los parámetros elegidos en cada caso, al tratarse de métodos no supervisados.

##  Diferenciación entre Data Drift y Concept Drift
¿Cómo cambia el rendimiento del modelo en situaciones de data drift y concept
drift?
Argumenta tu respuesta
- Andres: Tomando como métrica de referencia la precisión, notamos que bajo data drift, ésta métrica cae indicando un decaimiento en el desempeño del modelo, esto debido a que los datos con los que está prediciendo ya han cambiado con respecto a cuando se entrenó. Por otro lado, en el concept drift el target se ha dejado de relacionar a los datos, en este caso el cambio ha resultado en una mejora de desempeño del modelo pero no siempre será así, es por ello que es importante identificar cuando una caida en el desempeño del modelo se deba a un cambio en los datos de entrada o a un cambio en la relación de los mismos con el target.

## Evaluación de la Calidad de un Modelo de Machine Learning
Explica en tus palabras la evaluación del presente modelo de acuerdo a la precisión.

Explica en tus palabras la evaluación del modelo de acuerdo a la matriz de confusión
- Andrés: Al tener tanto una precisión como exactitud perfecta estamos ante un modelo que es consistente con sus predicciones y que cada una de ellas es correcta, es decir, las predicciones no son variadas u aleatorias y éstas son certeras de acuerdo al target. Por lo tanto, en este modelo no se cuentan con ningún tipo de errores de falsos positivos o falsos negativos en el conjunto de evaluación. Podríamos decir que este es un ejemplo de modelo ideal y al que se aspira llegar, sin embargo sabemos que en la vida real estos modelos son inalcansables.

