# advent of code
AOC="/c/GitHub/python/adventofcode"
AOC_COOKIE="..."

alias aos="cd $AOC; python -m solution < in.txt"
alias aot="cd $AOC; echo -ne '\\e[0;34m'; python -m solution < test.txt; echo -ne '\\e[0m'"
alias aoc="aot; echo; aos"

function aoc-load () {
    if [ $1 ]
    then
        curl --cookie "session=$AOC_COOKIE" https://adventofcode.com/$1/day/$2/input > in.txt
    else
        curl --cookie "session=$AOC_COOKIE" "$(echo `date +https://adventofcode.com/%Y/day/%d/input` | sed 's/\/0/\//g')" > in.txt
    fi
}