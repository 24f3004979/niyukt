vnv=$(ls -all | grep '.venv' && echo "True" || echo 'False')

if [ "${vnv}" == "True" ];then
  echo 'running venv exist script'
  source .venv/bin/activate
  echo "Sourced existing virtual environement 🌳"
else
  python3.12 -m venv .venv
  source .venv/bin/activate
  echo "Sourced new virtual environement 👾"
fi

pip install --upgrade pip
pip install -r requirements.txt
firefox http://127.0.0.1:8080/ &
echo "Launching application in countdown of 3 seconds : 🚀"
python app.py

