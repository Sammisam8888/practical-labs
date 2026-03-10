#!/bin/bash
set -e

compile_and_run() {
    local num=$1
    local name=$2
    local input=$3
    echo -e "\n============================================="
    echo "Testing Program $num: $name"
    echo "============================================="
    echo "Input: $input"
    yacc -d "10-03-26-0${num}-${name}.y"
    lex "10-03-26-0${num}-${name}.l"
    gcc lex.yy.c y.tab.c -lfl -o "p${num}" 2>/dev/null || gcc lex.yy.c y.tab.c -ll -o "p${num}"
    echo "$input" | "./p${num}"
}

compile_and_run 1 "valid-expression" "a+b*c"
compile_and_run 2 "nested-if" "if(a==b) { if(c==d) a=0; }"
compile_and_run 3 "arithmetic-expression" "1+3*4"
compile_and_run 4 "valid-variable" "hello_var"
compile_and_run 5 "evaluate-expression" "10+5*2"
compile_and_run 6 "an-bn" "aaabb"
compile_and_run 7 "an-b" "aaaaaaaaaaab"
