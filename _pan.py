import pandas as pd

info = [
    {"name": "pandas", "description": "Data analysis tool", "website": "https://pandas.pydata.org/"},
    {"name": "numpy", "description": "Numerical computing", "website": "https://numpy.org/"},
    {"name": "matplotlib", "description": "Data visualization", "website": "https://matplotlib.org/"}
]

data = pd.DataFrame(info)
