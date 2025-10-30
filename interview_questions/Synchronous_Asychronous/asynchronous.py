import asyncio

async def task(name):
    print(f"Starting {name}")
    await asyncio.sleep(5)
    print(f"Finished {name}")

async def main():
    await asyncio.gather(
        task("Task 1"),
        task("Task 2"),
        task("Task 3")
    )

asyncio.run(main()) 