from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dicomghost",
    version="0.1.0",
    description="Medical Device Network Traffic Analyzer for Security Assessments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Shantanu Shastri",
    url="https://github.com/shaan3000/dicomghost",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=["scapy>=2.5.0"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Security",
        "Topic :: System :: Networking :: Monitoring",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "dicomghost=dicomghost:main",
        ],
    },
)
