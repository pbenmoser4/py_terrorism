#Python Terror Stats Analysis

Using [python](https://www.python.org/) and associated tools to analyze data on global terrorist attacks over the past ~40 years.

The source for this data is the [Global Terrorism Database](https://www.start.umd.edu/gtd/), a project of [University of Maryland](http://www.umd.edu/).

## Data

### Github Data Size Restrictions

[Github](https://github.com/) has a default filesize restriction of `100.0MB`. As such, the data set being used in this project is not included in the git repo. This project assumes inclusion of the full terrorism dataset as available through the Global Terrorism Database, and looks for it at `src/terrorism.csv`.

Eventually, this will be generalized so that you can specify the file location in a more custom manner. But for now... deal with it `¯\_(ツ)_/¯`.
### Dowloading the Data

The data used can be found [here](https://www.start.umd.edu/gtd/contact/). Choose the `Download full GTD dataset` option from the dropdown menu, and fill in the associated fields to download the data.

---
## Tools Used

* [pandas](http://pandas.pydata.org/)
* [matplotlib](http://matplotlib.org/)
* [numpy](http://www.numpy.org/)
* [seaborn](https://stanford.edu/~mwaskom/software/seaborn/)
* [anaconda](https://docs.continuum.io/anaconda/)
  * Full download contains the [Conda](http://conda.pydata.org/docs/) package manager, as well as [Jupyter Notebook](http://jupyter.org/)
