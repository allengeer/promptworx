def call(exp):
    return eval(exp)

definition = {
            "name": "EVAL",
            "description": "Executes a simple python expression and returns the value.",
            "format": "EVAL <expression>",
            "call": call
}