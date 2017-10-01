# Clone Detection Through the Comparison of LLVM Intermediate Representation Blocks

Compare functions and detect software clones *(slowly)* at the IR level *(with lots of false positives)*

## Prerequisites

https://github.com/ztane/python-Levenshtein/

## Usage

Compile programs to be tested using LLVM and generate intermediate representation files (.ll)

Gather the files in a single directory

Run **Main.py**

Identifiy directory in which .ll files are located
```
C:\Users\User\Documents\ToTest
```

## Authors

**Tyler Elston**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* University of Alberta Highschool Internship Program
* Martin Oliveira
* Professor Nelson Amaral
* Antti Haapala - Levenshtein Implementation
