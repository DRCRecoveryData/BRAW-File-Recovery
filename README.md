# BRAW File Recovery

This repository contains a Python script that can be used to recover Blackmagic RAW (BRAW) video files. The script is based on the research and findings from DiskTuna and DRC Recovery.

## How it Works

The script searches for BRAW files by looking for specific signatures and extracts the data to create playable files. It uses a custom end signature that is determined by a set of rules based on specific conditions.

## Requirements

* Python 3.x
* pytsk3
* Enough disk space to store the recovered files
* An image of the disk containing the lost data

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/DRCRecoveryData/BRAW-File-Recovery.git
    ```

2. Install the required packages:

    ```bash
    pip install pytsk3
    ```

3. Run the script:

    ```bash
    python recover_braw.py
    ```

4. Follow the prompts to enter the image file path, the directory to save the recovered files, and the custom end signature.

## Disclaimer

This script is provided as-is and is intended for educational purposes only. The author of this script is not responsible for any data loss or damages that may occur. Use at your own risk.

## License

This project is licensed under the [MIT License](LICENSE).
