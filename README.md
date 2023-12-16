# Cuestionario de Monitoreo

## Creación de un dashboard para monitorear modelo de Datos
Explica cada una de las métricas que ves en el dashboard y has una interpretación de las
mismas respecto a lo que ves en las gráficas
- Andres: En el dashboard se muestran tres métricas del desempeño de nuetro clasificador binario: precisión, recall y exactitud. Intuyendo que la principal métrica del negocio es la precisión se puede tratar de un problema donde se buscan reducir los falsos positivos por encima de lo que obtendriamos de maximizar el recall en donde reduciriamos los falsos negativos o en la exactitud donde solo nos interesan las predicciones correctas. Particularmente en este modelo notamos que el desempeño del mismo fluctuó a lo largo de la ventana de tiempo teniendo máximos locales tanto en la precisión como el recall el 2 y 8  de enero. Sin embargo el comportamiento del modelo fue distinto en ambas fechas ya que para el 2 de enero se tuvo una reducción en la exactitud a pesar del aumento en la precisión del mismo día lo que significa que las predicciones tienen baja variabilidad pero no fueron muy cercanas al valor real. Caso contrario a lo que ocurre el 8 de enero en el que tanto la precición como la exactitud subieron en ese día indicando que las predicciones fueron consistentes y cercanas al valor real. De manera general habría que considerar una ventana más grande de tiempo de monitorio y conocer el contexto del problema para poder interpretar de mejor manera el desempeño de este modelo. 
