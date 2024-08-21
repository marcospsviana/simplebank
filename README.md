# simplebank

### ***This is not a real bank project is just to fun :) and practice***

### **how to set up and use this project**
*clone project*
~~~bash
git clone https://github.com/marcospsviana/simplebank.git
cd simplebank
python -m venv .venv
source .ven/bin/activate
~~~

### *How to test application*
~~~bash
python -m pytest tests -vss --postgresql-host=localhost --postgresql-password=postgres --postgresql-user=postgres --cov=simplebank tests/
~~~