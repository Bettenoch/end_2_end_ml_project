import os
import tarfile
import urllib.request # fetches data from a url 
import pandas as pd
from pathlib import Path # provides an object oriented way to handle file systems in paths

download_root = "https://github.com/ageron/data/raw/main/housing.tgz"

def load_housing_data():
    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(download_root, tarball_path)
        
    with tarfile.open(tarball_path) as housing_tarball:
        housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))

housing = load_housing_data()