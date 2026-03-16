import pandas as pd
import numpy as np

np.random.seed(42)
n = 80
data = {
    'muestra_id': [f'GW-{i:03d}' for i in range(1, n+1)],
    'pH':         np.round(np.random.normal(7.2, 0.8, n).clip(5.5, 9.5), 2),
    'Ca_mgL':     np.round(np.random.lognormal(3.5, 0.4, n), 2),
    'Mg_mgL':     np.round(np.random.lognormal(2.8, 0.5, n), 2),
    'Na_mgL':     np.round(np.random.lognormal(3.2, 0.6, n), 2),
    'HCO3_mgL':   np.round(np.random.lognormal(4.8, 0.3, n), 2),
    'SO4_mgL':    np.round(np.random.lognormal(3.1, 0.7, n), 2),
    'zona':       np.random.choice(['Norte', 'Sur', 'Centro'], n)
}
df = pd.DataFrame(data)
