from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import httpx
import os

load_dotenv(override=True)
gemini_api_key = os.getenv("GEMINI_API_KEY")

# check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Reference: https://ai.google.dev/gemini-api/docs
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    http_client=httpx.AsyncClient(verify=False)
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash-lite",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
