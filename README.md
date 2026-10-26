
# Text Tokenization Using Hugging Face Transformers

A beginner-friendly Natural Language Processing (NLP) project that demonstrates how to tokenize text using the pretrained BERT tokenizer from Hugging Face.

## Features

- Converts text into individual tokens
- Converts text into numerical token IDs
- Converts token IDs back into tokens
- Uses the pretrained BERT uncased tokenizer

## Technologies Used

- Python
- Hugging Face Transformers
- BERT
- Natural Language Processing (NLP)

## Model

`bert-base-uncased`

## Project Files

- `main.py` - Main Python application
- `requirements.txt` - Python dependencies

## Installation

1. Clone the repository:

   git clone https://github.com/akshatagurnale/Text-Tokenization

2. Navigate to the project directory:

   cd Text-Tokenization

3. Create a virtual environment:

   python -m venv .venv

4. Activate it on Windows:

   .venv\Scripts\activate

5. Install dependencies:

   pip install -r requirements.txt

## Usage

Run the program:

python main.py

## Example

Input:

Artificial Intelligence is amazing!

Output:

Tokens:
['artificial', 'intelligence', 'is', 'amazing', '!']

Token IDs:
[101, 7976, 4454, 2003, 6429, 999, 102]

Tokens from IDs:
['[CLS]', 'artificial', 'intelligence', 'is', 'amazing', '!', '[SEP]']

## What I Learned

- Text tokenization
- Subword tokenization
- Conversion of text into token IDs
- Using pretrained tokenizers with Hugging Face Transformers

## Author

AKSHATA GURNALE
