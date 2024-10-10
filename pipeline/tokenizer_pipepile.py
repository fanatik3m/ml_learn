from transformers import AutoTokenizer

model = 'bert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(model)
tokens = tokenizer.tokenize('It is time to tokenize')  # splitting the text to special tokens
print(tokens)

# in this example tokenizer make following actions to split the text to tokens
# -converting the text to lowercase
# -splitting the text using the special rules of subword-based tokenization

input_ids = tokenizer.convert_tokens_to_ids(tokens)  # mapping tokens to its unique id representations
print(input_ids)

final_inputs = tokenizer.prepare_for_model(input_ids)  # adding special tokens to both the beggining
print(final_inputs.get('input_ids'))                   # and the end of our number representations

inputs = tokenizer('It is time to tokenize')
modified_text = tokenizer.decode(inputs.get('input_ids'))

# example of high level tokenization
print(tokenizer('It is time to tokenize').get('input_ids'))