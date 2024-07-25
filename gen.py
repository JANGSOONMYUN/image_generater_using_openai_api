import requests
from PIL import Image
from io import BytesIO
import os
import json
import openai
from openai import OpenAI
import requests

def get_api_key(json_path):
    # Specify the path to your JSON file
    file_path = json_path
    # Load the JSON data from the file
    with open(file_path, 'r') as file:
        data = json.load(file)

    return data

def init_client():
    api_info = get_api_key('config.json')
    openai.organization = api_info['organization']
    openai.api_key = api_info['api_key']
    client = OpenAI(api_key=api_info['api_key'], organization=api_info['organization'])
    return client

def set_instruction_and_message(instruction, message):
    return [
        {"role": "system", "content": instruction},
         {"role": "user", "content": message}
    ]
    
def generate_prompt(client, img_name, instruction_image_analyst, instruction_dalle_converter, model='gpt-4o'):
    instruction = str(instruction_image_analyst)
    message = img_name
    messages = set_instruction_and_message(instruction, message)
    # print(messages)
    completion = client.chat.completions.create(
                        model=model,
                        messages = messages,
                        temperature=0.9,
                        max_tokens=4096
                    )
    result_str = completion.choices[0].message.content
    
    
    instruction = str(instruction_dalle_converter)
    message = result_str
    messages = set_instruction_and_message(instruction, message)
    completion = client.chat.completions.create(
                        model=model,
                        messages = messages,
                        temperature=0.9,
                        max_tokens=4096
                    )
    result_str = completion.choices[0].message.content
    return result_str


def generate_image(client, prompt, img_name):    
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1792",
        quality="hd",# hd, standard
        n=1,
    )
    
    image_url = response.data[0].url
    
    # 이미지 다운로드
    response = requests.get(image_url)
    
    # 이미지 저장
    if response.status_code == 200:
        with open(f'{img_name}.png', 'wb') as file:
            file.write(response.content)
        print('이미지가 성공적으로 저장되었습니다!')
    else:
        print('이미지 다운로드에 실패했습니다.')
