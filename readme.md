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

# Data Visualization
1. **Line Chart:** Countries vs Total Medals
2. **Bar Chart:** Countries vs Total number of Gold Medals
3. **Bar Chart:** Countries vs Total number of Silver Medals
4. **Bar Chart:** Countries vs Total number of Bronze Medals
5. **Histograms:** Countries Getting Gold, Silver, and Bronze in each Range.
6. **Exit to Main Menu**

# Data Analysis
1. **Print Records:** Top countries in terms of total medals won.
2. **Print Records:** Top countries in terms of total gold medals won.
3. **Print Records:** Top countries in terms of total silver medals.
4. **Print Records:** Top countries in terms of total bronze medals won.
5. **Print Records:** Bottom most countries in terms of medals won.
6. **Print Information:** General information about the data frame used for analysis.
7. **Describe Structure:** Describe the structure of the data frame used for analysis.
8. **Print Column Data:** Print the data of the column specified by the user.
9. **Print Maximum Values:** Display maximum values for each column in the data frame.
10. **Display Medals:** Display gold, silver, bronze medals won by a specific country.
11. **Go back to Main Menu**

# Data Manipulation
1. **Insert Row**
2. **Delete Row**
3. **Insert Column**
4. **Delete Column**
5. **Rename Column**
6. **Exit to Main Menu**


## Testing

To run the automated test suite, execute:

```shell
python -m unittest discover -s tests
