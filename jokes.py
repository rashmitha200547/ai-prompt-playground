from openai import OpenAI
client=OpenAI(api_key="your api key here")
model="gpt-4o-mini"
user_prompt=input("enter your prompt: ")
response=client.responses.create(model=model,input=user_prompt)
print(response.output_text)