import pandas as pd

seed_dataset = pd.read_csv("seeds_dataset.txt", sep="\s+", header=None)
seed_dataset.columns = [
    "area",               # A
    "perimeter",          # P
    "compactness",        # C = 4*pi*A/P^2
    "length",             # length of kernel
    "width",              # width of kernel
    "asymmetry",          # asymmetry coefficient
    "groove_length",      # length of kernel groove
    "LABEL"               # final column: class label
]
label_map = {
    1: "Kama",
    2: "Rosa",
    3: "Canadian"
}
seed_dataset["LABEL"] = seed_dataset["LABEL"].map(label_map)
seed_dataset_transformed = seed_dataset.groupby("LABEL", group_keys=False).apply(lambda x: x.sample(30, random_state=42))
seed_dataset_transformed.to_csv("seeds_dataset.csv", index=False)
print("Dataset saved with class labels as names and balanced 30 samples per class.")
