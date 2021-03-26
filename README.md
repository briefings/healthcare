
This exercise focuses on England's Public Health England [hospital activity data](https://www.england.nhs.uk/statistics/statistical-work-areas/covid-19-hospital-activity/), e.g.,

* [Monthly Publication](https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2021/02/Covid-Publication-11-02-2021.xlsx)

The programs herein include a few examples of reading data from multiple-sheet Microsoft Excel files.


<br>
<br>

### Development Notes

<br>

**Environment**

Refer to the [github.com/briefings/energy Development Notes](https://github.com/briefings/energy#development-notes), it outlines the
creation & usage of the environment `miscellaneous`, which is used by this repository also.

<br>

**Requirements**

```bash
    conda activate miscellaneous
    pip freeze -r docs/filter.txt > requirements.txt
```

whereby filter.txt does not include `python-graphviz`, `pywin32`, `nodejs`.  And, w.r.t. conventions

```bash
    pylint --generate-rcfile > .pylintrc
```

<br>

**Pending notebooks & notes**

* [healthcare.ipynb](https://colab.research.google.com/github/briefings/phe/blob/develop/notebooks/healthcare.ipynb)
