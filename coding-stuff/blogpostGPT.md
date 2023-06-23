
In this post, I wanted to share how I automated the data extraction project for my research. I have more than 2000 yearbooks in docx format that I want to extract data from. Before using chatgpt, I was trying to extract it with my own code. However, the files were not standard, some of them were ill-formatted and it was challenging to find a common pattern that applies to each. But asking chatgpt to do it solved my problem.

We need API access from openai to use chatgpt by Python. Signup at [https://platform.openai.com/](https://platform.openai.com). From personal in the up-right corner, go to "View API keys". Create a secret key and copy it for your application. Moreover, you need to go to billing on the same page and set up a payment method to be able to use this API key. It doesn't cost much and you can also set a monthly limit on your usage. 

We can start to code our program. We need docx and openai packages only (Note that, to download the docx package you need to use: pip install python-docx, not pip install docx). Then we enter the API key we generated

```python
import openai
import docx
openai.api_key = 'YOUR_API_KEY'
```

By using our docx library, we will read our docx files. I added two different functions for that purpose. This part is dependent on how your file is formatted. In my files, all information I need was embedded as tables instead of paragraphs, so I used the first one which convert all tables into text in a docx file. 

```python
def getText_tables(filepath):
    doc = docx.Document(filepath)
    fullText = []

    for table in doc.tables:
        
        for row in table.rows:

            rowtext = ""
            for cell in row.cells:
                rowtext = rowtext + "     " + cell.text
            
            fullText.append(rowtext)
    return '\n'.join(fullText)

def getText_paragraphs(filepath):
    doc = docx.Document(filepath)
    fullText = []

    for para in doc.paragraphs:
        
        fullText.append(para)
        
    return '\n'.join(fullText)

```

After getting our document as a string, now we can create a query by using this string and the question we have. In the function below, we create our input for chatgpt. You can modify it for your purpose. Our first argument is a string containing the document and the second one is the question we want chatgpt to answer by using the first argument. 

```python
def query_for_document(text_doc, question):
    query = f"""Use the below document to answer the subsequent question. If the answer cannot be found, write "I don't know."

    Document:
    \"\"\"
    {text_doc}
    \"\"\"

    Question: {question}"""
    return query

```
Now we can create a function that calls api and let chatgpt answer our question by query we created with the previous function. In this function, you can see that we are using the "gpt-3.5-turbo" model. This one is pretty efficient and cheap relative to gpt-4.0. You could check different models from openai website. Moreover, I assign a role to the chatgpt such that it can answer my question in this role. I told her to be a data extracting program fluent in Turkish and English since my documents contain both languages. It worked well for me but you might need to try different roles/questions/models to find which one works for you. 

<code>
    def get_chatgpt_answer_from_query(query):
        response = openai.ChatCompletion.create(
            messages=[
                {'role': 'system', 'content': 'You answer questions as a data extracting program fluent in Turkish and English.'},
                {'role': 'user', 'content': query},
            ],
            model="gpt-3.5-turbo",
            temperature=0,
        )

        return response['choices'][0]['message']['content']
</code>

We just completed the basics we need. The only thing left is running and checking if it runs properly. 

```python
myfile = "sirketyilliklari/1998/ADANA.docx"
text = getText_tables(myfile)
print(text)

```

         ADANA ÇİMENTO SANAYİİ T.A.Ş.
         KURULUŞ TARİHİ     :     05.10.1954
         (Established in)          
         BAŞLICA ÜRETİMİ     :     ÇİMENTO, KLİNKER, HAZIR BETON 
    İMALATI VE SATIŞI
         (Main Business Line)          (Cement, Clinker, Ready-Mix Concrete)
         GENEL MERKEZ     :     CEYHAN YOLU 12. KM 01321 – ADANA
         (Head Office)          
         GENEL MÜDÜR     :     ARİF GÜNGÖR TÜMER
         (General Manager)          
         YÖNETİM KURULU     :     HASAN IŞIK
         (Board of Directors)          HİKMET DİZDAROĞLU
                                               TUĞRUL HAYRETTİN ÖZANT
                                               OKTAY DİLEK
                                               METİN OKÇU
                                               YAŞAR ILIK
                                               ALİ MARALCAN
                                               
         TELEFON NO     :     (322) 332 99 50 / 7 HAT
         (Phone)          
         FAKS NO     :     (322) 332 95 01-332 97 32
         (Facsimile)          
         PERSONEL ve İŞÇİ SAYISI     :     567
         (Number of Employees)          
         TOPLU SÖZLEŞME DÖNEMİ     :     01.01.1998-31.12.1999
         (Collective Bargaining Period)          
         BAĞLI BULUNDUĞU İŞÇİ SENDİKASI     :     TÜRKİYE ÇİMSE-İŞ SENDİKASI
         (Labor Union)           
         BAĞLI BULUNDUĞU İŞVEREN SENDİKASI     :     TÜRKİYE ÇİMENTO MÜSTAHSİLLERİ 
    İŞVERENLERİ SENDİKASI
         (Employers' Union)          
         KAYITLI SERMAYE TAVANI     :     20.000.000.000.000.- TL
         (Authorized Capital)          
         ÇIKARILMIŞ SERMAYE     :     9.968.369.629.000.- TL
         (Issued Capital)          
         İŞLEM GÖRDÜĞÜ PAZAR     :     ULUSAL
         (Trading Market)          (National)


This string looks fine to me.
Let's ask our question. I wanted to extract board members and get it as a Python list.

```python

question = "What are the names of people in the board? Write the names only as a python list "
query = query_for_document(text, question)
answer = get_chatgpt_answer_from_query(query)
print(answer)
```

    ['HASAN IŞIK', 'HİKMET DİZDAROĞLU', 'TUĞRUL HAYRETTİN ÖZANT', 'OKTAY DİLEK', 'METİN OKÇU', 'YAŞAR ILIK', 'ALİ MARALCAN']

It looks pretty good. If you want to extract more information, you can make your question more detailed and you could want chatgpt to prepare it as a .json file. The rest will be up to you. 

I have tried using other LLM models in huggingface for this purpose, but they mostly answered me with only one name. They might work for you and you might give it a try. But I gave up using them for now and accepted the price. The price is like 600K words input ~ $1.5 and 600K words output ~ $2 which didn't seem like a big deal for me. 