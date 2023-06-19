```python
import openai
import pandas as pd
openai.api_key = 'YOUR API HERE'
```


```python

messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]
counter = 0
while counter < 1:
    print(counter)
    counter = counter +1
    message = "User : Could you write me an exam question for taking derivatives?"
    print(message)
    print("aftermessage")
    if message:
        print("inif")

        messages.append(
            {"role": "user", "content": message},
        )
        print("beforechat")

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        print("afterchat")
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
