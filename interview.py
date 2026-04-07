from openai import OpenAI
client=OpenAI(api_key="your api key here")
model="gpt-4o-mini"
system_prompt="You are an expert technical interviewer. Generate professional interview questions for the given topic and difficulty level. Do not include answers or formatting."
user_prompt=input("enter your prompt:")
messages=[{
    "role":"system",
    "content":[{
        "type":"input_text",
        "text":system_prompt
    }]
},
{
    "role":"user",
    "content":[{
        "type":"input_text",
        "text":user_prompt
    }]
},]
response=client.responses.create(model=model,input=messages)
print(response.output_text)

