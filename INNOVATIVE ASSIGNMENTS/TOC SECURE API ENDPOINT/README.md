
Theory of Computation — Interactive Toolkit
==========================================

This project provides an interactive Flask web app that implements key TOC concepts:
- Regular expression -> NFA (Thompson's construction)
- NFA -> DFA (subset construction)
- DFA minimization (partition refinement)
- Testing strings against NFA/DFA
- Visualizations (textual) and explanations for each step

What you get
- `app.py` - Flask web app with endpoints and UI
- `automata/regex_nfa.py` - regex parser & Thompson's NFA builder
- `automata/nfa_dfa.py` - subset construction & DFA minimization
- `templates/` - HTML templates (index, result, viz pages)
- `static/` - CSS/JS (minimal)
- `examples/` - sample regex and automata examples
- `requirements.txt` - Python deps

How to run
1. Create virtualenv and install:
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
2. Run:
   export FLASK_APP=app.py
   flask run --port=5004
3. Open http://127.0.0.1:5004/

