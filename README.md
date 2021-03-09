
This exercise focuses on England's Public Health England [hospital activity data](https://www.england.nhs.uk/statistics/statistical-work-areas/covid-19-hospital-activity/), e.g.,

* [Monthly Publication](https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2021/02/Covid-Publication-11-02-2021.xlsx)

The programs herein include a few examples of reading data from multiple-sheet Microsoft Excel files.


<br>
<br>

#### Development Notes

```bash
    conda install -c anaconda python=3.7
    
    conda install -c anaconda dask # installs: numpy, pandas
    conda install -c anaconda python-graphviz # installs: graphviz
    conda install -c anaconda pywin32 jupyterlab nodejs # installs: requests, urllib3
    conda install -c anaconda pytest coverage pylint pytest-cov
    
    conda install -c anaconda xlrd
```

For more information about Dask visit https://docs.dask.org/en/latest/install.html

<br>

**Requirements**

```bash
    conda activate phe
    pip freeze -r docs/filter.txt > requirements.txt
```

whereby filter.txt does not include `python-graphviz`, `pywin32`, `nodejs`.  And, w.r.t. conventions

```bash
    pylint --generate-rcfile > .pylintrc
```

<br>

**Extensions**

```bash
    conda activate phe
    jupyter labextension install @jupyterlab/toc
```

<br>

**Pending notebooks & notes**

* [phe.ipynb](https://colab.research.google.com/github/briefings/phe/blob/develop/notebooks/phe.ipynb)
