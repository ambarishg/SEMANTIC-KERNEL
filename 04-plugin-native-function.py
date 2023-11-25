import semantic_kernel as sk
from plugins.MathPlugin.Math import Math


async def main():
    # Initialize the kernel
    kernel = sk.Kernel()

    # Import the MathPlugin.
    math_plugin = kernel.import_skill(Math(), skill_name="MathPlugin")

    # Run the Sqrt function with the context.
    result = await kernel.run_async(
        math_plugin["Sqrt"],
        input_str="12",
    )

    print(result)


# Run the main function
if __name__ == "__main__":
    import asyncio

    asyncio.run(main())