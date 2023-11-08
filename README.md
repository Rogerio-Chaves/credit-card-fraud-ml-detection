# Credit Card Fraud Detection

<b>Author:</b> Rogerio Chaves

## Description:
<p align="justify">This project aim to detect fraud in credit card transaction. For this it use the <a href="https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023">Credit Card Fraud Detection Dataset 2023</a>. This dataset contains transactions made by European cardholders in the year of 2023. The data has been anonymized to protect the identities.</br>
Instances: 568.630 transactions</br>
Columns: </br>

- **id:** Unique identifier for each transaction;
- **V1 - V28:** Anonymized features representing various transaction attributes (e.g., time, location, etc);
- **Amount:** the transaction amount;
- **Class:** Binary label indicating whether the transaction is fraudulent (1) or not (0).</p>

**Dataset author:** Nidula Elgiriyewithana

## How to run this project:

### Get the datasets

<p>The instruction to get the datasets is in this <a href="https://github.com/Rogerio-Chaves/credit-card-fraud-ml-detection/blob/main/data/README.md">link</a></p>

OS used: Ubuntu 22.04.3 LTS

### Activate the virtual environment


<p>Open the terminal in the repository and set the command.</p>
<code>pip3 install pipenv</code></br>

<p>Active virtual environment.</p>
<code>pipenv shell</code></br>

#### Notebook file:

<p>With virtual environment activated, running the following command will create a kernel that can be used to run jupyter notebook commands inside the virtual environment.</p>
<code>ipython kernel install --user --name=venv</code></br>

<p>Finally, select the <b>venv</b> kernel in the notebook interface.</p>

#### Training Script file:

<p>With virtual environment activated, run the train script using this command <code>python3 train.py</code></p>

#### Predict web service:
<p>With virtual environment activated, build the dockerfile using this command<code>sudo docker build -t predict .</code></p>


<p>Finally, run docker with this command <code>sudo docker run -it -p 9696:9696 predict:latest</docker></p>


