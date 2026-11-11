# Aranyan T — Premium Flask Portfolio

A responsive multi-page portfolio built with **Python Flask, Jinja2, HTML, CSS and vanilla JavaScript**.

## Run locally (Windows PowerShell)

```powershell
python --version
python -m venv venv
.\\venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000. Stop with Ctrl+C.

If PowerShell blocks activation:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\\venv\\Scripts\\Activate.ps1
```

**Node.js and npm are not needed.** This is a Flask project, not React/Vite.

## Before publishing — personalize these

- Add your portrait as `static/images/profile.jpg`, then replace the initials placeholder in `templates/home.html`.
- Add your resume as `static/files/Aranyan_T_Resume.pdf`.
- Add your real email in `templates/contact.html` and `templates/partials/footer.html`.
- Add verified repository URLs to project cards. Placeholder repository links are deliberately not invented.
- Verify project descriptions, skills, event details and dates before sharing.
- CGPA is currently shown as 8.16/10; update if needed.

Known profile links:
- GitHub: https://github.com/Aranyan5
- LinkedIn: https://linkedin.com/in/aranyan-t

## Structure

```text
app.py
requirements.txt
README.md
PROMPT.md
templates/
  base.html, home.html, about.html, projects.html
  skills.html, experience.html, contact.html, 404.html
  partials/navbar.html, partials/footer.html
static/
  css/style.css
  js/main.js
  images/
  files/
instance/ (SQLite database is created automatically)
```

## Contact form

The form validates fields and stores submissions in `instance/portfolio.db`. It does **not** send email. Before public production use, add CSRF protection, rate limiting and spam protection. SQLite on ephemeral hosting may not persist; use a managed database for durable production storage.

## GitHub

Create an empty GitHub repository, then run from this folder:
```bash
git init
git add .
git commit -m "Build Flask portfolio"
git branch -M main
git remote add origin https://github.com/Aranyan5/aranyan-portfolio.git
git push -u origin main
```
Change the remote URL if you choose another repository name.

## Render deployment

Create a Render Web Service connected to GitHub:
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
- Add environment variable `SECRET_KEY` with a long random value.

Use a managed database for persistent contact messages. Add CSRF, rate-limit and spam protection before exposing the form publicly.
