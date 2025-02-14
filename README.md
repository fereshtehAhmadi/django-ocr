# django-ocr

A Django-based OCR (Optical Character Recognition) package that extracts text from images and provides structured data based on user-defined mappings.

## Features
- Extracts text from images using Tesseract OCR
- Supports Persian text recognition
- Allows users to define mappings for structured output
- Provides a simple API endpoint for image-to-text conversion

## Installation

Make sure you have Tesseract OCR installed on your system. You can install it using:

```bash
sudo apt install tesseract-ocr  # Ubuntu/Debian
brew install tesseract          # macOS
```
Then, install the package dependencies:
```bash
pip install -r requirements/base.text
```

## Usage
API Endpoint Run the Django server:
```bash
python manage.py runserver
```
Then, send a POST request to the API endpoint with an image file.

## Extract Raw Text
If no mappings are provided, the API returns the raw extracted text:
```bash
curl -X POST -F "image=@sample.jpg" http://127.0.0.1:8000/api/ocr/
```
Response:
````
{
  "raw_text": "نام: فرشته\nنام خانوادگی: احمدی"
}
````
## Extract Structured Data
Users can provide custom mappings for extracting specific fields:
````
curl -X POST -F "image=@sample.jpg" \
     -F 'mappings={"first_name": "نام", "last_name": "نام خانوادگی"}' \
     http://127.0.0.1:8000/api/ocr/
````
## Response:
````
{
  "raw_text": "نام: فرشته\nنام خانوادگی: احمدی",
  "structured_data": {
    "first_name": "فرشته",
    "last_name": "احمدی",
  }
}
````
## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License.