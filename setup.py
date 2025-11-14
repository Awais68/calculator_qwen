from setuptools import setup, find_packages

setup(
    name="calculator-app",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Flask==2.3.3",
        "gunicorn==21.2.0",
    ],
    author="Developer",
    description="A web-based calculator application",
    python_requires=">=3.12",
)