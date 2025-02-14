from setuptools import setup, find_packages

setup(
    name="django-ocr",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "django",
        "pytesseract",
        "Pillow",
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
    ],
)
