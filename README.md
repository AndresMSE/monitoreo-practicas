Cuestionario de Monitoreo

4. ¿Cómo cambia el rendimiento del modelo en situaciones de data drift y concept
drift?

Es posible observar una mejora en rendimiento del modelo en situación de concept drift y una baja en situación de data drift. El ejercicio ejemplifica la principal diferencia vista en clase, ya que el data drift sucede a partir de un cambio en la distribución de la data, por lo que es innevitable un desajuste en el modelo y una caída en el rendimiento del mismo. El concept drift, por otro lado, hace referencia a la relación entre las características y el target. Por ese motivo, no es posible afirmar que todo concept drift implica pérdida en rendimiento, al contrario, existe la posibilidad de la relación entre los dos aspectos antes mencionados se fortalezca y mejora, en consecuencia, nuestro rendimiento.

Ricardo: La presición del modelo inicial resultó 0.9, la presición del modelo con data drifting redujo a 0.89, debido a la introducción de nuevos datos aleatorios, por lo que se puede suponer que el modelo no está generalizando y se ve afectado por el cambio en las distribuciones.
La precisón del modelo con concept drifting es de 0.97, un incremento en la precisión con los datos antes de cualquier cambio. En este caso el modelo se adaptó o generalizó correctamente el cambio en la relación entre características y target.

5. Explica en tus palabras la evaluación del presente modelo de acuerdo a la precisión
De acuerdo con la precisión, de 30 flores iris, el 100% fue clasificada de la manera correcta. Es decir que el modelo funciona a la perfección.

Ricardo: En este caso la precisión del modelo fue de 100%, lo que indica que todas las predicciones fueron correctas para cada clase.


6. Explica en tus palabras la evaluación del modelo de acuerdo a la matriz de confusión
Debido a que, salvo por la diagonal principal, el resto de valores se encuentra en 0, es posible afirmar que
no hubo falsos positivos ni falsos negativos. Es decir que el modelo clasificó todas las flores bien y funciona a la perfección.

Ricardo: Como lo indica la precisión del modelo (100%) en la matriz de confusión se observan todos los valores en 0, fuera de la diagonal principal. Es decir, para cada clase todas las observaciones fueron prediichas correctamente.