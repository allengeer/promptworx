# Prompt Worx Prompt Engineering Automation Framework (PEAF)
import openai, re, os
from dotenv import load_dotenv

import eval
import readfile
import writefile

load_dotenv()

system_prompt = '''
You will be responding to user queries. User queries are designated 
in the format [USERQUERY] <messages>. 

You are also a controller for a system. You have a variety
of commands available that are defined below. You may use
any of these commands to respond to the USERQUERY messages. 

You do not have to use a command, and you can use commands multiple
times. To call commands, respond in the format of [COMMANDNAME] <PARAMETERS>.

For example, to use the EVAL command you would use

[EVAL] 5 + 7

The return of the command will be in the format [COMMANDRETURN] <return value>.

For example

[COMMANDRETURN] 12

When using commands, only use one command and nothing else.

When you are ready to respond to the user, please respond in the format 

[QUERYRESPONSE] <response>

Commands are defined as:
'''
sample_config = {
    "system" : system_prompt,
    "commands": [
        eval.definition,
        readfile.definition,
        writefile.definition
    ]
}

openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.organization = os.environ.get("OPENAI_ORG")


def generate_starter_messages():
    return add_message("system", generate_system_message())


def add_message(role, message, messages=[]):
    messages.append({"role": role, "content": message})
    return messages

def generate_system_message():
    return f"{sample_config['system']}\n{generate_commands_prompt()}"


def generate_commands_prompt():
    return "\n".join(map(lambda x: f"COMMAND NAME: {x['name']}\nDESCRIPTION: {x['description']}\nFORMAT: {x['format']}",
                         sample_config["commands"]))


def gptquery(messages, model="gpt-4", temperature=0.7):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    resp_text = response['choices'][0]["message"]["content"]
    print("PROCESSING: " + resp_text)
    return resp_text

def wrap(s, w):
    return [s[i:i + w] for i in range(0, len(s), w)]

def queryloop(messages):
    while True:
        resp = gptquery(messages)
        if re.match("\[QUERYRESPONSE\] (.+)", resp):
            print(re.match("\[QUERYRESPONSE\] (.+)", resp).groups()[0])
            break
        else:
            for command in sample_config["commands"]:
                command_match = re.match(f"\[{command['name']}\] (.+)", resp)
                if command_match:
                    if (command['name'] == "WRITEFILE"):
                        param_string = resp
                    else:
                        param_string = command_match.groups()[0]
                    try:
                        ret_text = wrap(command['call'](param_string), 3000)
                        for chunk in ret_text[:min(6, len(ret_text))]:
                            ret_string = f"[COMMANDRETURN] {chunk}"
                            print(ret_string)
                            messages = add_message("user", ret_string, messages)
                    except BaseException as e:
                        ret_string = f"[COMMANDRETURN] {str(e)}"
                        print(ret_string)
                        messages = add_message("user", ret_string, messages)




def userquery(query_text):
    queryloop(add_message("user", f"[USERQUERY] {query_text}", generate_starter_messages()))


if __name__ == "__main__":
    inp = input("How can I help you today? ")
    userquery(inp)