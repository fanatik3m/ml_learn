from transformers import AutoModelForSequenceClassification

checkpoint = 'distilbert-base-uncased-finetuned-sst-2-english'
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)

inputs = [
    '...',
    '... ...'
]

outputs = model(**inputs)
print(outputs.logits)
