### PHE

* https://docs.dask.org/en/latest/install.html

```bash
    
    conda install -c anaconda python=3.7
    
    conda install -c anaconda dask # installs: numpy, pandas
    conda install -c anaconda python-graphviz # installs: graphviz
    conda install -c anaconda pywin32 jupyterlab nodejs # installs: requests, urllib3
    conda install -c anaconda pytest coverage pylint pytest-cov
    
```

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

