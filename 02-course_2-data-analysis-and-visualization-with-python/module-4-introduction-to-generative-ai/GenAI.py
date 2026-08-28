
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = "Artificial Intelligence will transform the future of"

input_ids = tokenizer.encode(prompt, return_tensors="pt")

output_tokens = model.generate(
    input_ids,
    max_length=50,             
    num_return_sequences=1,     
    no_repeat_ngram_size=2,     
    temperature=0.7,            
    top_k=50,                   
    do_sample=True,             
    pad_token_id=tokenizer.eos_token_id
)

generated_text = tokenizer.decode(output_tokens[0], skip_special_tokens=True)

print("--- Generated Text ---")
print(generated_text)