import os
from langchain_core.messages import HumanMessage
from langchain_mistralai.chat_models import ChatMistralAI

from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["MISTRAL_API_KEY"]

chat = ChatMistralAI(api_key=api_key)

messages = [HumanMessage(content="knock knock")]
response = chat.invoke(messages)

# Classification
prompt = """
    You are a bank customer service bot. 
    Your task is to assess customer intent and categorize customer 
    inquiry after <<<>>> into one of the following predefined categories:

    card arrival
    change pin
    exchange rate
    country support 
    cancel transfer
    charge dispute

    If the text doesn't fit into any of the above categories, 
    classify it as:
    customer service

    You will only respond with the predefined category. 
    Do not provide explanations or notes. 

    ###
    Here are some examples:

    Inquiry: How do I know if I will get my card, or if it is lost? I am concerned about the delivery process and 
    would like to ensure that I will receive my card as expected. Could you please provide information about the 
    tracking process for my card, or confirm if there are any indicators to identify if the card has been lost during 
    delivery? Category: card arrival 
    Inquiry: I am planning an international trip to Paris and would like to inquire 
    about the current exchange rates for Euros as well as any associated fees for foreign transactions. Category: 
    exchange rate 
    Inquiry: What countries are getting support? I will be traveling and living abroad for an extended 
    period of time, specifically in France and Germany, and would appreciate any information regarding compatibility 
    and functionality in these regions. Category: country support 
    Inquiry: Can I get help starting my computer? I am 
    having difficulty starting my computer, and would appreciate your expertise in helping me troubleshoot the issue. 
    Category: customer service ###

    <<<
    Inquiry: {inquiry}
    >>>
    Category:
"""

prompt_improved = f"Please correct the spelling and grammar of \
this prompt and return a text that is the same prompt,\
with the spelling and grammar fixed: {prompt}"

messages = [HumanMessage(content=prompt_improved)]
response = chat.invoke(messages)
print(response.content)
