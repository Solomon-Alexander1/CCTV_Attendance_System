import pickle

ENCODINGS_FILE = "encodings.pickle"

with open(ENCODINGS_FILE, "rb") as f:
    data = pickle.load(f)

print("Pickle Data Type:", type(data))
print("Pickle Data:", data)
