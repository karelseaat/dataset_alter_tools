 # dataset_alter_tools
A versatile Python-based toolset for modifying and altering datasets, designed to streamline your machine learning workflow. This repository contains two primary tools: `crop-images.py` and `xml_to_yolo.py`.

## crop-images.py
**Functionality:** Automatically crops images in a specified directory to a fixed size of 640xN, maintaining the aspect ratio for optimal results.

### Usage
```bash
python crop-images.py /path/to/image/directory
```
Replace `/path/to/image/directory` with the desired image directory path. The script will list all the .png files in the specified directory, crop them to the desired size, and save each cropped image as a new .png file with a sequential index number.

## xml_to_yolo.py
**Functionality:** Converts annotated XML datasets (such as Pascal VOC) into YOLO format label files for easier integration with deep learning models.

### Usage
```bash
python xml_to_yolo.py /path/to/xml/directory
```
Replace `/path/to/xml/directory` with the directory path containing your annotated XML files. The script will convert all XML files in the specified directory to YOLO format label files (.txt) in the same directory, maintaining the original file names but replacing the extension.

### Dependencies
The following Python packages are required for both scripts:
- PIL (Pillow)
- xml.etree.ElementTree

Install these dependencies using pip:
```bash
pip install pillow
```

We hope this toolset will be helpful in your machine learning projects. Enjoy! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Happy coding! 😊