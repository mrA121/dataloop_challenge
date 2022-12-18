# Dataloop_challenge

### Steps to execute the program
1. Clone the repository using github url
````shell
git clone git@github.com:mrA121/dataloop_challenge.git
````
2. Change Directory to dataloop_challenge folder and create virtual environment and install dependencies
````shell
cd dataloop_challenge
python -m venv venv
pip3 install -r requirements.txt
````
3. Execute program with start_url, results can then be seen in the results.json file
````shell
python crawler.py <start_url: string> <depth: number>
````