# AI Finance Data Extractor

This is a mini project that extracts financial information such as company name, stock symbol, revenue, net income, and earnings per share (EPS) from any provided news article. The tool uses OpenAI's GPT-3.5 model to process the text and retrieve key financial metrics. The project is implemented using Streamlit for the web interface.

## Features

- **Extract Financial Information:** Automatically extracts key financial data from a text article.
- **Stock Symbol Retrieval:** Uses general knowledge to associate a stock symbol with the mentioned company.
- **Simple Interface:** Paste the news article, and the tool presents the extracted data in a clean dataframe.

## Files in the Repository

- `app.py`: Contains the main application logic using Streamlit to create the user interface.
- `helper.py`: Contains helper functions that interact with the OpenAI API to extract financial information from text.
- `__pycache__`: Automatically generated folder containing Python bytecode.
- `README.md`: The file you are reading now, containing documentation for the project.

## How It Works

The application works in two main parts:

1. **User Input:** The user pastes a news article into a text box.
2. **Data Extraction:** When the user clicks the "extract" button, the app uses OpenAI's GPT model to extract financial information, which is then displayed in a dataframe.

## Example

Given an input news article:

```
Tesla's earnings this quarter blew all estimates. They reported $4.5 billion profit against a revenue of $30 billion. Their earnings per share was $2.3.
```

The tool extracts the following data:

| Measure       | Value         |
|---------------|---------------|
| Company Name  | Tesla         |
| Stock Symbol  | TSLA          |
| Revenue       | $30 billion   |
| Net Income    | $4.5 billion  |
| EPS           | $2.3          |

## Installation and Setup

To run this project locally, follow the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/NitinYadav1511/AI-Finance-Data-Extractor.git
   cd AI-Finance-Data-Extractor
   ```

2. Install dependencies:
   Make sure you have Python installed. Install the required libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` doesn't exist, you'll need to install `streamlit`, `pandas`, and `openai` manually:
   ```bash
   pip install streamlit pandas openai
   ```

3. Set up OpenAI API key:
   - Get your API key from OpenAI.
   - In `helper.py`, replace the placeholder `<your openai api key>` with your actual OpenAI API key:
     ```python
     openai.api_key = "<your openai api key>"
     ```

4. Run the Streamlit App:
   Start the Streamlit app using the command:
   ```bash
   streamlit run app.py
   ```

5. Open in Browser:
   Once the app is running, a local server will start, and you can access the tool in your web browser.

## Usage

1. Paste the financial news article in the provided text area.
2. Click on the "Extract" button.
3. View the extracted financial data in the resultant dataframe on the right side of the app.

## Dependencies

- Python 3.7+
- OpenAI API (`openai`)
- Streamlit (`streamlit`)
- Pandas (`pandas`)

## Future Improvements

- Add error handling for invalid or incomplete articles.
- Improve stock symbol retrieval accuracy.
- Implement additional financial metrics extraction.

## Contributor

This repository is maintained by [Nitin Yadav](https://github.com/NitinYadav1511).

## License

This project is open-source and available under the MIT License.
