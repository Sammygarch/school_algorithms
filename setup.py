from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = "school_algorithms",
    version = "1.1.2",
    author = "Sammy Garcia",
    author_email = "s@mmygarcia.com",
    description = "School algorithm module for Python",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Sammygarch/school-algorithms.git",
    project_urls = {
        "Bug Tracker": "https://github.com/Sammygarch/school-algorithms/issues"
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Education"
    ],
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    python_requires = ">=3.6",
)