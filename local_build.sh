pipenv install --dev
pipenv run rm -rf public
pipenv install --skip-lock
pipenv run reflex init
pipenv run reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
cp vercel.json public/