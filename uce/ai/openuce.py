import openai
from pydantic import BaseModel

openai.organization = 'org-PYELIbA8LxpnGFiTsMHVkbOV'
openai.api_key = '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'


class Document(BaseModel):
    item: str = ''


def process_inference(user_prompt) -> str:
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un un profesor de programación universitario"},
            {"role": "user", "content": user_prompt}
        ]
    )
    response = completion.choices[0].message.content
    return response
