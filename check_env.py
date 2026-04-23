# -*- coding: utf-8 -*-
import sys
import chemprop
import torch
import pandas
import numpy
import sklearn

print(f"[OK] Python version: {sys.version}")
print(f"[OK] Chemprop version: {chemprop.__version__}")
print(f"[OK] Torch version: {torch.__version__}")
print(f"[OK] Pandas version: {pandas.__version__}")
print(f"[OK] Numpy version: {numpy.__version__}")
print(f"[OK] Scikit-learn version: {sklearn.__version__}")

from chemprop.args import TrainArgs, PredictArgs
print("[OK] Chemprop core modules imported successfully!")