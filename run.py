from gen import init_client, generate_prompt, generate_image
from instructions import instruction_image_analyst, instruction_dalle_converter
target_names = [
    [
    "Two of Wands", "Three of Wands", "Four of Wands", "Five of Wands"
    ],
    [
    "Six of Wands", "Seven of Wands", "Eight of Wands", "Nine of Wands", "Ten of Wands",
    ]
]  



if __name__ == "__main__":
    target_name = target_names[0]
    client = init_client()
    for tname in target_name:
        print(tname)
        for i in range(5):
            prompt = generate_prompt(client, tname, instruction_image_analyst, instruction_dalle_converter)
            print('prompt ok')
            generate_image(client, prompt, f'{tname}_{i}')
            print(i)

