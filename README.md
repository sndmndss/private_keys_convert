# Private Keys Converter

## Overview

The Private Keys Converter is a utility script designed to transform a default list of accounts with associated keys for the MEME platform into corresponding addresses. It is tailored to work with a standard account list format, such as: `123;123;3214214321`.

## Prerequisites

Before you begin, ensure you have Python installed on your system. You can download the latest version of Python from the official website at [python.org](https://www.python.org/).

## Getting Started

To use the Private Keys Converter, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/sndmndss/private_keys_convert
   ```

2. Navigate to the cloned directory:
    ```bash
    cd private_keys_convert
   ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Prepare your accounts table in HTML format and save it as `List1.html` in the project directory.

5. Run the script:
    ```bash
   python script.py
   ```

## Usage Instructions

- The script expects an HTML file named `List1.html` containing the accounts table.
- After execution, the script will output the converted addresses.



