import pickle
from pyexpat import model

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)