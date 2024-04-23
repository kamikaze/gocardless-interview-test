import asyncio

from interview.api.client import go_cardless


async def main():
    print('Interview')

    await go_cardless.main()


asyncio.run(main())
