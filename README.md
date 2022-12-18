# Dataloop_challenge

### PreRequisites
1. Python3
2. Venv (Package for creating virtual environments in python)

### Steps to execute the program
1. Clone the repository using github url
````shell
git clone git@github.com:mrA121/dataloop_challenge.git
````
2. Change Directory to dataloop_challenge folder and create virtual environment and install dependencies
````shell
cd dataloop_challenge
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
````
3. Execute program with start_url, results can then be seen in the results.json file
````shell
python crawler.py <start_url: string> <depth: number>
````