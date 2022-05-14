# Function Plotter
a GUI program that plots arbitrary user-entered function.

![picture alt](https://github.com/Snossy123/Function-Plotter/blob/main/test/function%20plot%20ex.png "TopologyManager UML")

## Description
- Take a function of x from the user, e.g., 5*x^3 + 2*x.
1. Take min and max values of x from the user.
2. The following operators must be supported: + - / * ^.
3. The GUI should be simple and beautiful (well organized).
4. Apply appropriate input validation to the user input.
5. Display messages to the user to explain any wrong input.
6. You may use programming language and platform of your choice.
7. You must test your program. Include the testing codes in your repository.
8. Your code should be well organized and well documented.

## Why Python is used as the programming language
- Python today is one of the most popular simple universal languages for **data visualization** and even more. It is often the best choice for solving problems in Machine Learning, Deep Learning, Artificial Intelligence, and so on. It is object-oriented, easy to use, and developer-friendly due to its highly readable code.
- By using Python codes, one can easily automate their industrial tasks, and can also reach an advanced level of automation. In **automation software testing**, Python is considered to be a performance booster. For **automation tools**, the developers are required to write only a few lines of code. like [Unittest](https://docs.python.org/3/library/unittest.html), The unittest **unit testing framework** was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages.

## Used Technologies
- [PyCharm](https://www.jetbrains.com/lp/pycharm-anaconda/) as an IDE.
- [matplotlib](https://matplotlib.org/) as a Visualization tool.
- [tkinter](https://docs.python.org/3/library/tkinter.html) to Build GUI.
- [Unittest](https://docs.python.org/3/library/unittest.html) to perform unit tests. 

## Function Plotter Documentation
**Function Plotter is modeled by Five Functions as follows:**

- ***program_GUI Function:*** Provides the user with Simple and butty `GUI`.
- ***validate_input Function:*** Provides User With `Messages box` if he entered Wrong Input format.
- ***validate_eq Function:*** Provides User With Messages box if he entered Wrong `Equation` format.
- ***check_user_input Function:*** Provides User With `Messages box` if he entered Wrong Range of Values of X format.
- ***plot Function:*** Provides User With `butty graph` of Equation formula.


**snapshots of working
and wrong examples:**

**Valid Input (equation & min x & max x) :**

![picture alt](https://github.com/Snossy123/Function-Plotter/blob/main/test/test1%20valid%20Input.jpg "TopologyManager UML")

**Valid Input (equation & min x & max x) :**

![picture alt](https://github.com/Snossy123/Function-Plotter/blob/main/test/test2%20valid%20Input.jpg "DataBase UML")

**InValid Input (equation) :**

![picture alt](https://github.com/Snossy123/Function-Plotter/blob/main/test/test1%20Invalid%20Input.jpg "TopologyManager UML")

**InValid Input (min x | max x) :**

![picture alt](https://github.com/Snossy123/Function-Plotter/blob/main/test/test2%20Invalid%20Input.jpg "DataBase UML")


## Usage
- Install the [Used Technologies](#Used-Technologies).
- Import style & regex packages in your program, ex:
```
from qbstyles import mpl_style
import re
```

## Testing
- Unit tests is provided by `test` file which is defined [here](https://github.com/Eslam-Walid/TopologyAPI/blob/master/src/test/java/TestTopologyAPI/TestTopologyAPI.java).
- `test.py` contains test methods for all `program` methods.
- You can run the whole `test.py` class or run individual methods.
- Output of [unittest](https://docs.python.org/3/library/unittest.html) testing process from [pycharm](https://www.jetbrains.com/lp/pycharm-anaconda/):

![picture alt](https://github.com/Snossy123/Function-Plotter/blob/main/test/autotest.jpg "Testing Output")
