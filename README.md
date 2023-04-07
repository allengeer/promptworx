# promptworx
Prompt Worx is a prompt automation solution that provides a framework for introducing automation into prompt responses from ChatGPT.

# WARNING - USE AT YOUR OWN RISK
This is an experimental library and very likely introduces significant security 
risks to the environment which is executed - as it basically executes code directly
from ChatGPT. This code is provided with no warranty. 

Use at your own risk.

# Configuration
This code requires an Open AI API key. You can set these values in environment variables
or a .env file. The two variables required are 

OPENAI_API_KEY - Your OpenAI API Key

OPENAI_ORG - Your OpenAI Organisation Key 

#  Usage
Running the module root in a main thread will execute a query prompt in the command
console. You can submit your query here. From there the system will query ChatGPT
at which point it may respond in a variety of system command prompts.  When ChatGPT
has arrived at a response it will respond. 

# Commands
PromptWorx allows users to provide ChatGPT a variety of commands that it can execute
to help service queries. To add a command simply provide the command entry in the
configuration file as well as the function to execute the command.