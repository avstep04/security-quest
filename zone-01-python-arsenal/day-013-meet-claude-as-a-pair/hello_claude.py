import anthropic
from dotenv import load_dotenv

load_dotenv()                   # puts ANTHROPIC_API_KEY from .env into the environment
client = anthropic.Anthropic()  # the SDK reads ANTHROPIC_API_KEY automatically

message = client.messages.create(
    model="claude-haiku-5-5",   # fast and inexpensive, good for learning
    max_tokens=2000,
    messages=[{"role": "user", "content": "In two sentences: what's the difference between hashing and encryption?"}],
)
answer = "".join(block.text for block in message.content if block.type == "text")
print(answer)
print(f"\nTokens: {message.usage.input_tokens} in, {message.usage.output_tokens} out")