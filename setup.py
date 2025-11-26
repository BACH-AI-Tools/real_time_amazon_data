"""Setup script for real_time_amazon_data"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="real_time_amazon_data",
    version="1.0.0",
    author="BACH Studio",
    author_email="contact@bachstudio.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BACH-AI-Tools/real_time_amazon_data",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        # 添加你的依赖
    ],
)
