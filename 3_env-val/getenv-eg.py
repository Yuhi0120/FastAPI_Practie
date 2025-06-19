import os

name = os.getenv("MY_NAME", "World")
print(f"Hello {name} from Python")

#usage
#Here we don't set the env var yet
# python main.py

# 💬 As we didn't set the env var, we get the default value

# Hello World from Python

# 💬 But if we create an environment variable first
# export MY_NAME="Wade Wilson"

# 💬 And then call the program again
# python main.py

# 💬 Now it can read the environment variable

# Hello Wade Wilson from Python