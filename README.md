# Random Word generator using linux's dictionary

Expects dictionary to be either `/usr/share/dict/words` or `/usr/dict/words`, or passed in as an argument

Will generate 5 words, or however many is passed as an argument.

```
python3 random_words.py [-nw | --num-words number] [-d | --dictionary path_to_dictionary_file]
```

Can add a function to `.bashrc`:
```
function random_words() {
    python3 path/to/file/random_words.py "$@"
}
```

and call it with 

```
random_words [-nw | --num-words number] [-d | --dictionary path_to_dictionary_file]
```
