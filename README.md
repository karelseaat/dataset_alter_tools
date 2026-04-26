 # dataset_alter_tools
A practical Python toolset for modifying and altering datasets, aimed at simplifying your machine learning workflow. This repository encompasses two main tools: `crop-images.py` and `xml_to_yolo.py`.

## crop-images.py
**Functionality:** Automatically crops images within a specified directory to a fixed size of 640xN, preserving the aspect ratio for optimal results.

### Usage
To use this tool, run the following command in your terminal:
```bash
python crop-images.py /path/to/image/directory
```
Replace `/path/to/image/directory` with the desired image directory path. The script will list all .png files in the specified directory, crop them to the desired size, and save each cropped image as a new .png file with a sequential index number.

## xml_to_yolo.py
**Functionality:** Transforms annotated XML datasets (such as Pascal VOC) into YOLO format label files for seamless integration with deep learning models.

### Usage
To use this tool, run the following command in your terminal:
```bash
python xml_to_yolo.py /path/to/xml/directory
```
Replace `/path/to/xml/directory` with the directory path containing your annotated XML files. The script will convert all XML files in the specified directory to YOLO format label files (.txt) in the same directory, maintaining the original file names but replacing the extension.

### Dependencies
Both scripts require the following Python packages:
- Pillow (PIL)
- xml.etree.ElementTree

Install these dependencies using pip:
```bash
pip install pillow
```

We hope this toolset will be beneficial in your machine learning projects. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request. Enjoy coding! 💻

## More from Karelseaat

For more projects and experiments, visit my GitHub Pages site: [karelseaat.github.io](https://karelseaat.github.io/)
