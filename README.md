# coding-challenge

Select the directory for the language you wish to use, JavaScript or Python. Challenges are the same for both languages. Within your prefered language's directory you will see 7 nested directories, one for each challenge. Each challenge has it's own README.md that explains what is expected for the specific challenge.

To start clone the main branch and then checkout to a new branch and make it your name. `git checkout -b 'kelly-sorbello`

The challenges `rnaTranscription`,`hamming` and `spaceAge` are the 'easy' challenges. You can start with those if you'd like, all the rest are about the same difficulty level.
Each challenge has its own tests for you to check your work. The goal is to complete as many as you can and whoever gets the most done within the coding challenge time slot will be the winner and recieve extra engage points.

Once you're done or time is up, please push up your branch for Theo and I to look at. Have fun!


All challenges were pulled from the site exercism.io [https://exercism.io](https://exercism.io)

## Making the test suite pass - Javascript

Execute the tests with:

```bash
$ npm test
```

In the test suites all tests but the first have been skipped.

Once you get a test passing, you can enable the next one by changing `xtest` to
`test`.

## Running the tests - Python

To run the tests, run `pytest [py_test_file]`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest [py_test_file]`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`
