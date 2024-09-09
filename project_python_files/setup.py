# Sample of setup.py file for a python project
from setuptools import setup, find_packages

setup(
    name="my_project",  # Project name
    version="0.1.0",  # Project version
    description="A brief description of the project",  # Short description
    long_description=open('README.md').read(),  # Long description, usually the README file
    long_description_content_type="text/markdown",  # Content type of long description (markdown, reStructuredText)

    author="Your Name",  # Author's name
    author_email="your.email@example.com",  # Author's contact email

    url="https://github.com/yourusername/my_project",  # URL for the project (usually GitHub or project homepage)

    packages=find_packages(),  # Automatically find and include all packages in the project
    include_package_data=True,  # Include additional files from MANIFEST.in

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",
    ],

    python_requires=">=3.6",  # Minimum Python version required
    install_requires=[  # List of dependencies
        "requests",
        "numpy"
    ],

    entry_points={  # Console scripts or entry points for the package
        'console_scripts': [
            'my-command=my_project.module:main_function',
        ],
    },
)
