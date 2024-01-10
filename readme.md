# <h1 align="center">Python Data Manipulation and Visualization Project</h1>

## Project Overview

This project is a robust Python application designed for data manipulation and visualization. It provides tools for modifying CSV files and generating insightful histograms from the dataset. It's particularly tailored for analyzing and visualizing the World Championship Data Set Visualization (WCDSV), focusing on the distribution of medals among participants.

## Features

- **Data Manipulation**: Easily insert and delete rows and columns within the CSV dataset.
- **Column Management**: Rename existing columns as needed.
- **Data Visualization**: Create histograms to showcase the distribution of medals.
- **Interactive CLI**: Navigate project features through a user-friendly command-line interface.

## Installation

### Prerequisites

Before you begin, make sure you have Python 3.6 or higher installed, as well as pip for managing Python packages.

### Setup

Clone the repository and install the required dependencies:

------------------------------------------------------------------------------------------------------

## Quick Start

To get the application up and running on your local machine, follow these steps:

1. Clone the project repository:

    ```shell
    git clone https://github.com/Srijan-Baniyal/PythonProject
    ```

2. Navigate to the project directory:

    ```shell
    cd your-project-repository
    ```

3. Install the required packages:

    ```shell
    pip install -r requirements.txt
    ```

4. Run the main script:

    ```shell
    python main.py
    ```

Follow the command-line interface prompts to manipulate the dataset or to visualize the data.

## Usage

### Data Manipulation

- **Insert Rows**: Select the insert row option and enter the data for the new row.
- **Delete Rows**: Choose the delete row option and specify the index of the row to be removed.
- **Insert Columns**: Choose the insert column option and provide the name and data for the new column.
- **Delete Columns**: Select the delete column option and enter the name of the column to be removed.

### Visualization

Select the visualization option from the main menu to generate histograms and analyze the medal distribution in the dataset.

## Documentation

For comprehensive documentation on modules and usage, please see the `/docs` directory within the project.

## Testing

To run the automated test suite, execute:

```shell
python -m unittest discover -s tests
