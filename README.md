# Pdf Resizer Python

## Description
Pdf Resizer Python is a simple tool to resize PDF files. It allows users to change the dimensions of PDF pages to fit their needs, whether for printing, sharing, or archiving.

## Features
- Resize PDF pages to custom dimensions
- Maintain aspect ratio while resizing
- Batch processing of multiple PDF files
- Command-line interface for easy integration into scripts

## Installation
To install the Pdf Resizer Python tool, you need to have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

To resize all PDF files in a folder, use the following command:

```bash
python3 main.py [folder] [scale_factor]
# Example: python3 main.py /path/to/folder 0.5
```


with specific size
```bash
python3 main.py [folder] [width] [height]
# Example: python3 main.py /path/to/folder 400 600
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or suggestions, please open an issue on the GitHub repository.
