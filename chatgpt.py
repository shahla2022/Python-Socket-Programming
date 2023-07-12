import openai
API_KEY="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"
open.api_key=API_KEY

Completion=openai.Completion.create(model="text-davinchi-003",prpmpt="write say hello project with react",max_Tokens=7,
                                  temperature=0.5
                                  )
response=Completion.choices[0].text
print(response)