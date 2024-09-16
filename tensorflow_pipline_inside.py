from transformers import AutoTokenizer, TFAutoModel, TFAutoModelForSequenceClassification
import tensorflow as tf

model_checkpoint = 'distilbert-base-uncased-finetuned-sst-2-english'

# get tokenized inputs
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

raw_inputs = [
    'text1',
    'text2.....'
]
tokenized_inputs = tokenizer(raw_inputs, padding=True, truncation=True, return_tensors='tf')

# get tensor representation
model = TFAutoModel.from_pretrained(model_checkpoint)
outputs = model(tokenized_inputs)
print(outputs.last_hidden_state.shape)

# get model's output values (logits)
model = TFAutoModelForSequenceClassification.from_pretrained(model_checkpoint)
outputs = model(tokenized_inputs)
print(outputs.logits)  # model's output as logits

# get final result from logits using softmax
predictions = tf.math.softmax(outputs.logits, axis=-1)
print(predictions)  # final result from numbers that actually sum up to 1

# convert outputs from softmax to actual labeled classification
labels_result = model.config.id2label
print(labels_result)