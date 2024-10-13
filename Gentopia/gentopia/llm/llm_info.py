# Listing available LLMs

TYPES = {
    "gpt-3.5-turbo": "OpenAI",
    "gpt-4o-mini": "OpenAI",
    'text-davinci-003': "OpenAI",
    "gpt-4": "OpenAI",
    "gpt-3.5-turbo-16k": "OpenAI",
    "gpt-4-32k": "OpenAI",
    "gpt-3.5-turbo-0613": "OpenAI",
    "gpt-4-0613": "OpenAI",
    "gpt-3.5-turbo-16k-0613": "OpenAI",
    "gpt-4-32k-0613": "OpenAI",
    "t5-vicuna-3b": "Huggingface",
    "replit-3b": "Huggingface",
    "camel-5b": "Huggingface",
    "mpt-7b": "Huggingface",
    "redpajama-7b": "Huggingface",
    "redpajama-instruct-7b": "Huggingface",
    "alpaca-lora-7b": "Huggingface",
    "alpaca-lora-13b": "Huggingface",
    "kullm": "Huggingface",
    "stablelm-7b": "Huggingface",
    "os-stablelm-7b": "Huggingface",
    "flan-3b": "Huggingface",
    "baize-7b": "Huggingface",
    "gpt4-alpaca-7b": "Huggingface",
    "vicuna-7b": "Huggingface",
    "baize-13b": "Huggingface",
    "vicuna-13b": "Huggingface",
    "gpt4-alpaca-13b": "Huggingface",
    "flan-11b": "Huggingface",
    "stable-vicuna-13b": "Huggingface",
    "camel-20b": "Huggingface",
    "starchat-15b": "Huggingface",
    "starchat-beta-15b": "Huggingface",
    "evolinstruct-vicuna-7b": "Huggingface",
    "evolinstruct-vicuna-13b": "Huggingface",
    "guanaco-7b": "Huggingface",
    "guanaco-13b": "Huggingface",
    "guanaco-33b": "Huggingface",
    "falcon-7b": "Huggingface",
    "falcon-40b": "Huggingface",
    "wizard-falcon-7b": "Huggingface",
    "wizard-falcon-40b": "Huggingface",
    "airoboros-7b": "Huggingface",
    "airoboros-13b": "Huggingface",
    "samantha-7b": "Huggingface",
    "samantha-13b": "Huggingface",
    "samantha-33b": "Huggingface",
    "wizard-vicuna-30b": "Huggingface",
    "wizardlm-13b": "Huggingface",
    "wizardlm-30b": "Huggingface",
}

COSTS = {
    "gpt-3.5-turbo": {"prompt": 0.0015 / 1000, "completion": 0.002 / 1000},
    "gpt-4": {"prompt": 0.03 / 1000, "completion": 0.06 / 1000},
    "gpt-3.5-turbo-16k": {"prompt": 0.003 / 1000, "completion": 0.004 / 1000},
    "gpt-4-32k": {"prompt": 0.06 / 1000, "completion": 0.12 / 1000},
    "gpt-3.5-turbo-0613": {"prompt": 0.0015 / 1000, "completion": 0.002 / 1000},
    "gpt-4-0613": {"prompt": 0.03 / 1000, "completion": 0.06 / 1000},
    "gpt-3.5-turbo-16k-0613": {"prompt": 0.003 / 1000, "completion": 0.004 / 1000},
    "gpt-4-32k-0613": {"prompt": 0.06 / 1000, "completion": 0.12 / 1000},
}
