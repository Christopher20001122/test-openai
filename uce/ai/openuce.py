import openai
from pydantic import BaseModel

openai.organization = 'org-PYELIbA8LxpnGFiTsMHVkbOV'
openai.api_key = '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'


class Document(BaseModel):
    item: str = 'pizza'


def process_inference(user_prompt) -> str:
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un chef que lista los ingredientes de los platillos que se te proporcionan.
        E.G
        pan
        Ingredientes:
        arina
        huevos
        agua
        azucar
        ...
        """},
            {"role": "user", "content": user_prompt}
        ]
    )
    response = completion.choices[0].message.content
    return response
