from setuptools import find_packages, setup

setup(
    name="Ecommercebot",
    version="0.0.0",
    author="Nagendra",
    author_email="maddela3435@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain-google-genai','datasets','pypdf','python-dotenv','flask']
)