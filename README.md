# Kenneth E. Batcher - Document Cataloging and OCR

Dr. Kenneth E. Batcher is a highly accomplished Emeritus professor of Computer Science at Kent State University.  He has received many prestigious awards like the IEEE Seymour Cray and ACM/IEEE Eckert-Mauchley Award.  He discovered the Batcher Odd-Even Mergesort and Bitonic Sorter.  And, he holds, or is affiliated with, 14 US Patents.  His work in computer science and parallel processing earned him a place in history as a PP-father.

More information can be found about him here:
- [Kenneth E. Batcher Wiki](https://en.wikipedia.org/wiki/Ken_Batcher)
- [Kenneth E. Batcher Faculty Profile](https://www.kent.edu/cs/kenneth-e-batcher)

Unfortunately, during my time at Kent State University, Dr. Batcher passed away.  As a tribute to him and in an effort to preserve his legacy/work, the computer science department opened a project to scan, document, and curate his work for archival, posting to a memorial website, and donation to a computer science museum in Irvine, CA.

To that end, this project was created.

My objective is to conduct an OCR-analysis on the scanned documents of Dr. Batcher's work.  I intend to do some natural language processing on the results and create some interesting visualizations (like a word cloud) to potentially contribute to his memorial website.  In any case, I feel that by doing this work I am learning about a esteemed man and his contribution to computer science.

## Demo

![Final Results](link-to-image)

## Getting Started

Windows:
Get Windows Subsystem for Linux (WSL) and pdf2image.  You can follow this['link to medium article'] installation and usage guide.
Use pip to get the required imports.
Create the appropriate directories, 'images' and 'pdfs'.
Provide some pdfs in the pdf-directory.

## Running the OCR-analysis

Once you have completed the 'Getting Started':
Run the 'go_OCR' script with a terminal command like 'python go_OCR'.

## Built With

* [Python 3](https://www.python.org/download/releases/3.0/) - General Purpose Programming Language
* [Pytesseract](https://pypi.org/project/pytesseract/) - Python OCR Wrapper
* [pdf2Image](https://pypi.org/project/pdf2image/) - Python PDF to Image Converter
* [Teseract-OCR](https://en.wikipedia.org/wiki/Tesseract_(software)) - OCR Utility
* [Poppler](https://en.wikipedia.org/wiki/Poppler_(software)) - PDF Utility

## Authors

* **Matthew E. Miller** - *Initial work* - [Github](https://github.com/matmill5)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

TODO:
There is a group of KSU students from Fall '19 and Spring '20 which have created a memorial website for Dr. Batcher.  I will try to find a link to their content.
