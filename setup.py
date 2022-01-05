from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = "school_algorithms",
    version = "0.0.8",
    author = "Sammy Garcia",
    author_email = "s@mmygarcia.com",
    description = "School algorithm module for Python",
    long_description = long_description,
    py_modules = ["school_algorithms"],
    long_description_content_type = "text/markdown",
    url = "https://github.com/Sammygarch/school-algorithms.git",
    project_urls = {
        "Bug Tracker": "https://github.com/Sammygarch/school-algorithms/issues"
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires = ">=3.6",
)
