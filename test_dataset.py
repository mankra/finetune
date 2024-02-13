from datasets import load_dataset, load_from_disk

# dataset = load_from_disk(
#     "./endless-sky.hf",
#     #data_dir="data",
#     #split="train",
#     #use_auth_token=True,
#     #num_proc=4,
#     #streaming=False,
# )

from datasets import load_dataset

dataset = load_dataset(
    "ossbig2024/endless-sky-master",
    split="train",
)

# dataset = load_dataset(
#     "ossbig2024/endless-sky-master",
#     data_dir="data",
#     data_files="train-*",
#     split="train",
#     use_auth_token=True,
#     num_proc=4,
#     streaming=False,
#     #ignore_verifications=True,
# )
#
dataset = dataset.train_test_split(
        test_size=0.005, seed=0, shuffle=True
    )
train_data = dataset["train"]
valid_data = dataset["test"]

print (train_data)
print (valid_data)
