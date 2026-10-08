RUN ON YOUR COMPUTER
  pip install -r requirements.txt
  python app.py        -> open http://127.0.0.1:5000

UPDATE CONTENT: edit profile_data.py (everything on the site comes from it).

DEPLOY FREE ON RENDER (Flask needs a Python host; workers.dev cannot run Flask)
  1. Upload this folder to a new GitHub repo.
  2. render.com > New > Web Service > connect the repo.
  3. Build command: pip install -r requirements.txt
     Start command: gunicorn app:app
  4. Use the .onrender.com link on LinkedIn and your resume.
Keep your FinSight site (floral-meadow...) as it is. This is a separate site.
