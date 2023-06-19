Lets import openai library and enter our openai api we generated from [platform.openai.com](platform.openai.com)
```python
import openai
import pandas as pd
openai.api_key = 'YOUR API HERE'
```

In the code below, we make chatgpt to write us an exam question about taking derivatives. In the first message we specify chatgpt's capabilities. Since it is cheaper and still effective, I prefer "gpt-3.5-turbo" as the model. Denote that, you need to set up a payment method before being able to use api. You can also set a monthly usage limit to make sure it will not exceed some amount. You will pay as much as you used. No recurring payment or fix cost. 

```python

messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]

print(counter)

message = "User : Could you write me an exam question for taking derivatives?"
print(message)

if message:
    messages.append(
        {"role": "user", "content": message},
    )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
reply = chat.choices[0].message.content
print(f"ChatGPT: {reply}")
messages.append({"role": "assistant", "content": reply})
```


```python
f = open("yearbookstxt/1998/ECYAP.txt", "r")
yearbook = f.read()
query = f"""Use the below document to answer the subsequent question. If the answer cannot be found, write "I don't know." 

Document:
\"\"\"
{yearbook}
\"\"\"

Question: Write all the information in this document as a json file"""
```


```python
response = openai.ChatCompletion.create(
    messages=[
        {'role': 'system', 'content': 'You answer questions as an data extracting program fluent in Turkish and English.'},
        {'role': 'user', 'content': query},
    ],
    model="gpt-3.5-turbo",
    temperature=0,
)

print(response['choices'][0]['message']['content'])
```
