# smar

**S**tring **MA**ss **R**eplace: replace test strings in files across a directory tree.

## Overview

Do you need to perform mass replacement of text strings in files? Do you have one or maybe several various text strings to replace? Should the replacement be done in a single or several files? In any of these cases `smar.py` will do the job for you.  


## How it works?
`Smar.py` is a [Python](https://www.python.org/doc/essays/blurb/) script that takes a list of strings to find and replace, traverses directory tree and does all the replacements. 

The list of replacements is provided in a file. Each line of the file contains a string to find and string to replace separated with a tab. You may provide one or several lines that should be replaced. 

Directory to search is entered inside the `smar.py` script. You may do the replacement in a single file or several files. If provided directory contains subdirectories, they will be searched as well.

## How to run it?

* [Download](https://www.python.org/downloads/) and Install Python, if you do not have one installed already.

* Save script `smar.py` somewhere on your PC.

* Prepare a file `replacements.txt` that contains a list like below:

  ```
  some text to replace	a new text to use instead
  this is wrong 	that is better
  nice	very nice
  ...
  ```

* Save `replacements.txt` in the same directory where you put `smar.py`.
  
* open script `smar.py` and in line below enter the path to directory with files that should be updated:

  ```python
  dir_to_process = 'C:/Users/Krzysztof/Documents'
  ```

  If you are using Windows, then replace backslashes `\` with forward-slashes `/` so they are looking like in example above.

* Run the script `python smar.py`. This will show all occurrences of strings in files. No any single replacement has been made at this point.

* If you are ready to made the replacements, then run the script with option `–u`, i.e.: `python smar.py -u`.



## Requirements

To run, this application needs Python. Get it and install from https://www.python.org/downloads/.

## License

This code is in the Public Domain (or CC0 licensed, at your option). Unless required by applicable law or agreed to in writing, this software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
