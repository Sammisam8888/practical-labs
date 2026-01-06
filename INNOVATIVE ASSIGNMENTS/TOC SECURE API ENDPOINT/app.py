
from flask import Flask, render_template, request, redirect, url_for
from automata.regex_nfa import regex_to_nfa, nfa_to_dot, simulate_nfa
from automata.nfa_dfa import nfa_to_dfa, simulate_dfa, minimize_dfa, dfa_to_dot
import json, os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY','devkey')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/build', methods=['POST'])
def build():
    regex = request.form.get('regex','').strip()
    if not regex:
        return redirect(url_for('index'))
    try:
        nfa = regex_to_nfa(regex)
        nfa_dot = nfa_to_dot(nfa)
        dfa = nfa_to_dfa(nfa)
        dfa_dot = dfa_to_dot(dfa)
        min_dfa = minimize_dfa(dfa)
        min_dot = dfa_to_dot(min_dfa)
        return render_template('result.html', regex=regex, nfa_dot=nfa_dot, dfa_dot=dfa_dot, min_dot=min_dot)
    except Exception as e:
        return render_template('index.html', error=str(e), regex=regex)

@app.route('/test', methods=['POST'])
def test():
    automaton = request.form.get('automaton','dfa')  # 'nfa' or 'dfa'
    expr = request.form.get('expr','').strip()
    string = request.form.get('string','')
    if automaton == 'nfa':
        nfa = regex_to_nfa(expr)
        ok = simulate_nfa(nfa, string)
        return render_template('test_result.html', automaton='NFA', expr=expr, string=string, accepted=ok)
    else:
        nfa = regex_to_nfa(expr)
        dfa = nfa_to_dfa(nfa)
        ok = simulate_dfa(dfa, string)
        return render_template('test_result.html', automaton='DFA', expr=expr, string=string, accepted=ok)

if __name__ == '__main__':
    app.run(debug=True)
