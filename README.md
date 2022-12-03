# Classify documents

This project classifies documents according to keywords found within said documents.

## Installation

This project was tested on Ubuntu 22.04 and Windows 10. It will probably run on any OS with Python3.

On Windows: if needed, install Python. You can get Python from https://python.org.
Note: Make sure to check "Include Python in the Path" when installing.

Install dependencies: Run `pip3 install -r requirements.txt`.

## Assumptions

- It is assumed that all the documents to be classified are each under its own folder. All those folders are located in the "top level folder".
- It is assumed that there are some words that appear in each of the documents that classify them.
- It is assumed that the documents are in either .docx or .pdf format.
- It is assumed that no folders with names matching the the classifiers exist in the top lever folder.

## Using the software

Run `python classify.py`. The programme will output errors for each file in the top level folder that is not of the correct format.
Once prompted, enter each classifier, then hit enter, and once done, hit enter twice.
The programme will output errors for each file not matching any of the classifiers.
The programme will move each file matching a classifier to a folder titled with that classifier (for example, all files containing the classifier "foo" will be moved to a folder named "foo", while all files containing the classifier "bar" will be moved to a folder named "bar"), and move the rest of the files into a folder titled "No_match".
The programme will create a .yaml file titled "Word_Frequency_All_Sorted.yaml" containing all the words in the documents, sorted by frequency.


## Author

**Shalom Mitz** - [shalommmitz](https://github.com/shalommmitz)

Thanks to Dor Mitz for giving feedback and writing part of the README.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE ) file for details.

