# Gradio OpenAI Chat

This project is a simple chat application built using Gradio that allows users to interact with OpenAI's API. Users can input text and receive responses from the AI model.

## Project Structure

```
gradio-openai-chat
├── src
│   ├── app.py          # Entry point of the application
│   └── utils
│       └── openai_client.py  # Handles OpenAI API interactions
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd gradio-openai-chat
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Open the `src/app.py` file and enter your OpenAI API key in the designated field.
2. Run the application:
   ```
   python src/app.py
   ```
3. A Gradio interface will open in your browser, allowing you to chat with the AI.

## API Key

Make sure to obtain your OpenAI API key from the OpenAI website and enter it in the application to enable functionality.

## License

This project is licensed under the MIT License.