import subprocess

dependencies = [
    "web3",
    "python-dotenv"
]

for dependency in dependencies:
    subprocess.check_call(["pip", "install", dependency])
