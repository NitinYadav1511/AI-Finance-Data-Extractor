import openai
import json
import pandas as pd

#openai.api_key = "<your openai api key>"

def get_prompt():
    return '''Please retrieve company name, revenue, net income and earnings per share (a.k.a. EPS)
    from the following news article. If you can't find the information from this article 
    then return "". Do not make things up.    
    Then retrieve a stock symbol corresponding to that company. For this you can use
    your general knowledge (it doesn't have to be from this article). Always return your
    response as a valid JSON string. The format of that string should be this, 
    {
        "Company Name": "Walmart",
        "Stock Symbol": "WMT",
        "Revenue": "12.34 million",
        "Net Income": "34.78 million",
        "EPS": "2.1 $"
    }
    News Article:
    ============

    '''
    

def extract_financial_info(text):
    prompt = get_prompt()+text

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        message = [{'role':'user', 'content':prompt}]
    )
    content = response.choices[0]['message']['content']
    
    try:
        json.loads(content)
        return pd.DataFrame(data.items(), columns = ['Measure', 'Value'])
    except (json.JSONDecodeError, IndexError):
        pass

    return pd.DataFrame({'Measure': ['Compamy Name', 'Stock Symbol', 'Revenue', 'Net Income', 'EPS'],
                         'Value': ["", "", "", "" ""]})
    return content

if __name__ == "__main__":
    text = """Tesla's Earning news in text format: Tesla's earning this quarter blew all the estimates. They reported 4.5 billion $ profit against a revenue of 30 billion $. Their earnings per share was 2.3 $"""
    data = extract_financial_info(text)