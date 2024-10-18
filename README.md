# Python Projects Collection

This repository contains a variety of Python projects showcasing different programming concepts, from web development and automation to API integrations and data scraping. Each project is designed to demonstrate practical applications of Python, using frameworks such as Flask, along with third-party APIs and libraries.

## Projects

### 1. **To-Do List App (Flask)**
A simple To-Do list web application built using Flask. Users can add tasks, mark them as complete, and remove them from the list.

- **Features**:
  - Add and remove tasks
  - Mark tasks as complete
  - Flask backend with basic HTML templates
- **Instructions**:
  1. Navigate to the `toDo_app` directory.
  2. Install dependencies with `pip install -r requirements.txt`.
  3. Run the Flask app with `python app.py`.

### 2. **Typing Speed Test (Tkinter)**
A desktop application that allows users to test their typing speed by comparing the number of words typed within a set time limit.

- **Features**:
  - Displays sample text for the user to type
  - Tracks typing speed in words per minute (WPM)
- **Instructions**:
  1. Navigate to the `typing_speed_test` directory.
  2. Run the application with `python typing_speed_test.py`.

### 3. **NBA Player Stats Scraper**
A web scraper that extracts NBA player statistics from Basketball Reference and saves them into a CSV file using BeautifulSoup and Pandas.

- **Features**:
  - Scrapes NBA player statistics for a given season
  - Saves the scraped data in a CSV file
- **Instructions**:
  1. Navigate to the `nba_stats_scraper` directory.
  2. Install the required packages with `pip install -r requirements.txt`.
  3. Run the script with `python scrape.py`.

### 4. **Barcode Lookup (Flask + Cloudmersive API)**
A Flask-based web application that allows users to enter a barcode and retrieve product information using the Cloudmersive Barcode API.

- **Features**:
  - Input a barcode to retrieve product information
  - Uses the Cloudmersive Barcode API for lookup
- **Instructions**:
  1. Navigate to the `barcode_lookup` directory.
  2. Install dependencies with `pip install -r requirements.txt`.
  3. Add your Cloudmersive API key in `app.py`.
  4. Run the Flask app with `python app.py`.


### 5. **Watermark GUI (Tkinter + Pillow)**
A desktop application built using Tkinter that allows users to upload an image and add a text watermark automatically.

- **Features**:
  - Upload any image
  - Add a custom text watermark to the image
  - Save the watermarked image
- **Instructions**:
  1. Navigate to the `watermark_GUI` directory.
  2. Install the required libraries with `pip install -r requirements.txt`.
  3. Run the application with `python watermark_app.py`.

### 6. **Morse Code Converter (Command-Line)**
A Python command-line program that converts any string input into Morse code.

- **Features**:
  - Converts text to Morse code
  - Can handle letters, numbers, and common punctuation
- **Instructions**:
  1. Navigate to the `morse_code_converter` directory.
  2. Run the script with `python morse_code_converter.py`.
 
### 7. **Downloads Folder Organizer**
A Python script that organizes your Downloads folder by automatically sorting files into subfolders based on their file types (e.g., Documents, Images, Videos, etc.).

- **Features**:
  - Automatically moves files into predefined subfolders (Documents, Images, Music, etc.)
  - Creates subfolders if they don't exist
  - Categorizes files by extensions and moves unrecognized files to an "Others" folder
- **Instructions**:
  1. Navigate to the `downloads_organizer` directory.
  2. Edit the path in the `organize_downloads.py` script to point to your Downloads folder.
  3. Run the script with `python organize_downloads.py`.

## How to Contribute

Feel free to fork this repository, submit issues, and make pull requests. Contributions and improvements are welcome!

## License

This repository is open-source under the MIT License. Feel free to use it for your own projects.
