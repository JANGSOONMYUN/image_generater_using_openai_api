# Image Generator

This project generates card images based on given instructions using OpenAI's GPT-4 and DALL-E models. The process involves three main steps:

1. **Analyze the Input Target**: Interpret the input card name.
2. **Generate a Prompt for DALL-E**: Create a detailed prompt for generating an image using DALL-E.
3. **Create an Image Using DALL-E**: Use the generated prompt to create and save an image.

## Project Structure

- `gen.py`: 
  - Contains functions for initializing the OpenAI client, setting instructions and messages to the model, generating prompts, and creating images.
  
- `run.py`: 
  - Main script to execute the image generation process for a list of target card names.
  
- `instructions.py`: 
  - Contains pre-set instructions for the models to follow during prompt generation and image generation.
  
- `config.json`: 
  - A JSON file that contains the necessary API keys and organization information for OpenAI.

## Prerequisites

- Python 3.8+
- Install required packages:
  ```sh
  pip install requests Pillow openai
  ```

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/JANGSOONMYUN/image_generater_using_openai_api
    cd image_generater_using_openai_api
    ```

2. **Prepare `config.json`**:
    - Create a `config.json` file in the root directory with your OpenAI API information:

      ```json
      {
        "organization": "YOUR_ORGANIZATION_ID",
        "api_key": "YOUR_API_KEY"
      }
      ```

3. **Run the script**:
    ```sh
    python run.py
    ```

## Content of `config.json`

Your `config.json` should contain the following information:

```json
{
  "organization": "YOUR_ORGANIZATION_ID",
  "api_key": "YOUR_API_KEY"
}
```

Replace `"YOUR_ORGANIZATION_ID"` and `"YOUR_API_KEY"` with your actual OpenAI organization ID and API key.

## How It Works

### gen.py

- **get_api_key(json_path)**: Loads API key and organization info from the specified JSON path.
- **init_client()**: Initializes the OpenAI client using the API information.
- **set_instruction_and_message(instruction, message)**: Sets the instructions and messages for the model.
- **generate_prompt(client, img_name, instruction_image_analyst, instruction_dalle_converter, model='gpt-4o')**: 
  Generates a prompt for the DALL-E model using GPT-4.
- **generate_image(client, prompt, img_name)**: Uses the generated prompt with DALL-E to create and save an image.

### run.py

- Sets up target card names.
- Initializes the OpenAI client.
- Iterates through the target names, generating prompts and images, and saving the results.

### instructions.py

Contains the pre-set instructions for generating detailed prompts and converting these prompts for the DALL-E model. These instructions ensure the generated images adhere to a standard structure and stylistic guidelines.

## Customization

You can customize the list of target names in `run.py` and the instructions in `instructions.py` to generate different cards or images with different themes.