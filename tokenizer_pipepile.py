from transformers import AutoTokenizer

model = 'bert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(model)
inputs = tokenizer('It is time to tokenize')
print(inputs['input_ids'])