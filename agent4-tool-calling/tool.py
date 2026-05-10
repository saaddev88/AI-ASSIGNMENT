from agents import Agent, Runner, function_tool, RunContextWrapper
import asyncio
from connection import config
from dataclasses import dataclass


@dataclass
class UserInfo:
    name: str
    uid: int


@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[UserInfo]) -> str:
    return f"User {wrapper.context.name} is 22 years old."


async def main():
    user_info = UserInfo(name="Hafiz Syed Hassan Nadeem", uid=66)

    agent = Agent[UserInfo](
        name="Assistant",
        # instructions="use the `fetch_user_age` tool to get the user's age.",
        tools=[fetch_user_age]
    )

    result = await Runner.run(
        starting_agent=agent,
        input="What is the age of the user?",
        context=user_info,
        run_config=config
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
