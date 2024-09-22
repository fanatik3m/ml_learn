from transformers import AutoTokenizer

model = 'bert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(model)
tokens = tokenizer.tokenize('It is time to tokenize')  # splitting the text to special tokens
print(tokens)

# in this example tokenizer make following actions to split the text to tokens
# -converting the text to lowercase
# -splitting the text using the special rules of subword-based tokenization