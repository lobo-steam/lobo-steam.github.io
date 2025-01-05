pip install --user pipenv
pipenv install --dev
pipenv run pip install --upgrade pip
pipenv install -r requirements.txt
rm -rf public
pipenv run reflex init
pipenv run reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
cp vercel.json public/
