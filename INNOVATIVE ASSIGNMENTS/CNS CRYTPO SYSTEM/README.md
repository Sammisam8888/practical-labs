
# CNS Flask Project - Cryptocurrency Network Security (Sample Implementation)

This repository contains a full Flask-based codebase scaffold for a project on Cryptocurrency Network Security (CNS).
It includes backend (Flask + SQLAlchemy), frontend templates (dark UI using Tailwind CDN), sample modules to simulate simple network/attack flows, and example reports.

## What is included
- `app/` - main Flask application package
  - `app/__init__.py` - app factory and configuration
  - `app/models.py` - SQLAlchemy models (User, SimulationResult)
  - `app/routes.py` - main routes and API endpoints
  - `app/simulate.py` - simulation & analysis utilities for network/attack simulation
  - `app/templates/` - Jinja2 templates (dark UI)
  - `app/static/` - static assets (css, js)
- `scripts/` - helper scripts (generate sample report)
- `requirements.txt` - Python dependencies
- `run.sh` - small helper to run the app (Linux/macOS)
- `cns_flask_project.zip` - this packaged archive (created by this script)

## Quick start (Linux/macOS)
1. Create a virtualenv and install requirements:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   export FLASK_APP=app
   export FLASK_ENV=development
   flask run --host=0.0.0.0 --port=5000
   ```
3. Open http://localhost:5000 in your browser.

## Notes for your assignment
- The code is intentionally commented and modular to help you explain design choices in your report.
- The `simulate` module contains demonstrative functions (network latency, double-spend risk estimation, node failure simulation) — you can expand them based on your coursework depth.
- Templates are placed under `app/templates` as you requested (UI only inside templates folder).

If you want, I can now:
- Add authentication flows (login/register)
- Add more detailed simulation models or visualizations
- Create sample data & screenshots
