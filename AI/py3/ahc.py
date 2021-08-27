import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from math import sqrt
import pandas as pd

path='C:\Users\Usuario\Desktop\IA\proyecto3\df_pc.csv'

df=pd.read_csv(path)

