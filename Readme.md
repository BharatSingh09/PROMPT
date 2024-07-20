# Resume Parser

This project contains a script that uses OpenAI's GPT API to parse a resume and convert its content into a structured JSON format. 

## Requirements

- Python 3.x
- OpenAI Python package

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/resume-parser.git
    cd resume-parser
    ```

2. Install the OpenAI package:
    ```bash
    pip install openai
    ```

## Usage

1. Set your OpenAI API key in the script. Replace `your-openai-api-key` with your actual OpenAI API key:
    ```python
    openai.api_key = 'your-openai-api-key'
    ```

2. Run the script with the resume text:
    ```bash
    python parse_resume.py
    ```

3. The script will print the parsed JSON format of the resume content.

## Example

### Resume Text Input
