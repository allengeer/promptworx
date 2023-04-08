import os.path


def call(content):
    with open("out.txt", 'w') as file:
        file.write(content)
        file.close()


definition = {
            "name": "WRITEFILE",
            "description": "Writes the text out to a file on the file system ",
            "format": "WRITEFILE <filename> <content>",
            "call": call
}