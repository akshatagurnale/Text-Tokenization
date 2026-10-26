from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "Artificial Intelligence is amazing!"

tokens = tokenizer.tokenize(text)

print(tokens)

ids = tokenizer.encode(text)
print(ids)

print(tokenizer.convert_ids_to_tokens(ids))

