import numpy as np
import pandas as pd
import os
# Crear datos de ejemplo
np.random.seed(42)
dates = pd.date_range(start='2022-01-01', end='2022-01-10', freq='D')
model_metrics = pd.DataFrame({
'Fecha': dates,
'Precision': np.random.uniform(0.8, 0.95, len(dates)),
'Recall': np.random.uniform(0.7, 0.9, len(dates)),
'Exactitud': np.random.uniform(0.85, 0.98, len(dates))
})
model_metrics.to_csv(os.path.abspath('./data/model_metrics.csv'),header=True, index=False)