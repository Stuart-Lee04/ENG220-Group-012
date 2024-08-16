# Air Quality Streamlit App

This project is a Streamlit application to implement a data dashboard for the state of New Mexico to visualize Water, Air Quality, Health and Finance data. 

## Prerequisites

- Python
- Conda
- Streamlit

## Getting Started

### Install Python, Python Env and streamlit 

- Install the required Python packages and a virtual environment. We will be using python 3.8 for this project.
- Download and Installation instructions for different operating systems on [python.org](python.org).
- Download and Installation instructions for conda are different operating systems are available on [anaconda.org](anaconda.org).
- Install streamlit libraries in the python environment and ensure all the libraries and working and are installed. Instruction are available on [[https://docs.streamlit.io/](https://docs.streamlit.io/)).
- All of these instructions are compiled in this page [https://docs.streamlit.io/get-started/installation/anaconda-distribution](https://docs.streamlit.io/get-started/installation/anaconda-distribution)

### Clone the Repository

First, clone the repository to your local machine:

```sh
git clone https://github.com/Tsriram95/data_dashboard
cd data_dashboard
```

### File and directory structure

- The directory names should be pretty self explanatory.
- 'analysis' consists of the python code for the analysis and visualization.
- This is where the streamlit app runs from and consists of the parent page, streamlit_app.py (First page of the data dashboard application).
- 'analysis/pages' will consist of the different pages for different types of data (like water, air, finance, health etc).
- 'data' will have the raw data that is collected and should be stored in the respective directories of the type of data similar to analysis, in the above point.

### Working on your streamlit page

- You can refer to the template we have in the analysis directory or work on you own streamlit app to show your visualizations. There are many examples of such visualizations and data representation on [streamlit.io/gallery](streamlit.io/gallery) and [https://github.com/streamlit](https://github.com/streamlit)
- Once you are satified or want to test your page to see how it renders, you can use the following command from the directory of your page (replace with the name of 'your_page').

```
streamlit run <your_page.py>
```

- If you have issues with the above command, use:

```
python -m streamlit <your_page.py>
```
