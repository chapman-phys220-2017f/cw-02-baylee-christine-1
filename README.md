# PHYS220 CW 2

**Author(s):** **CHANGEME**

## Specification

Complete the following exercises, placing your solutions into separate files. Remember to use the templates in the `info` repository as a guide for what you should include in your source files. In each file, write the solution as a callable function.

0. **Exercise 0**
  
  **Familiarize yourself on IPython and Jupyter**
  
  With your partner, go through the [IPython/Jupyter Slides](https://slides.com/profdressel/jupyter-overview). Be sure to play with both `ipython3` in a terminal and with Jupyter in the notebook interface within CoCalc. Go through the Help menu for Jupyter together.
  
1. **Exercise 1**  (`coord.py`)
  
  **Generate equally spaced coordinates**
  
  *Idea:* Generate $n + 1$ equally spaced $x$ coordinates in the interval $[a, b]$. Store
the coordinates in a list.

  (a) Create a function `coord_for(n, a=0, b=1)` that takes three parameters: `n` is the integer number of intervals, `a` is the interval left endpoint, and `b` is the interval right endpoint. Note that the endpoints `a` and `b` are keyword parameters with default values of `0` and `1`, respectively. To generate the coordinates, start with an empty list, then use a for loop and append each equally spaced `x` coordinate to the list. Return the completed list.
  
  *Hint:* With $n$ intervals, corresponding to $n + 1$ points, in $[a, b]$, each interval has length $h = (b−a)/n$. The coordinates can then be generated by the formula $x_i = a + i\,h, i = 0, \ldots , n + 1$.
  
  (b) Create a function `coord_while(n, a=0, b=1)` that does the same thing as in (a), but uses a while loop instead of a for loop

  (c) Create a function `coord_comp(n, a=0, b=1)` that does the same thing as in (a), but uses a list comprehension instead of a for loop.
  
1. **Exercise 2** (```fibs.py```)
  
  **Generate Fibonacci numbers**
  
  *Idea:* Generate the first `n` Fibonacci numbers. Recall that the Fibonacci numbers are obtained by summing the previous two numbers to generate the next number. The sequence starts traditionally with $[1,1]$, yielding $[1,1,2,3,5,8,\ldots]$ as the sequence.
  
  (a) Create a function `fibs(n)` that takes one positive integer parameter `n` and returns a list of the first `n` Fibonacci numbers.
  
  (b) Create a function `fib_generator()` that returns a generator (i.e., using the `yield` keyword instead of `return`) for the next Fibonacci number, starting with the number $1$. Done correctly, the following code should return the list `[1,1,2,3,5]` :
  ```python
  g = fib_generator()
  [next(g) for _ in range(5)]
  ```
  
1. **Exercise 3** (```converge.py```)
  
  **Compute convergent sum**
  
  *Idea:* Compute the following "infinite" sum: $$\sum_{k=1}^\infty \frac{1}{k^2} \equiv \lim_{N\to\infty} \sum_{k=1}^N \frac{1}{k^2}$$
  
  *Note:* It is impossible to actually add an infinite number of terms in practice. We rely on the fact that this sum is *convergent* to compute an approximate value. That is, the terms that contribute to the sum steadily get smaller as $k$ increases. To exploit this fact, we specify a *tolerance* (small value) such that when the next term of the sum is below this tolerance, we truncate the sum and treat the remainder as negligible.
  
  (a) Create a function `compute_sum(tol=1e-2)` that returns the value of the sum. The keyword parameter `tol` specifies a tolerance. Stop the summation when the next term of the sum would be smaller than this tolerance.
  
  (b) Show to what value does the sum converges as you let the tolerance become smaller and smaller.

**Notebook:** To cleanly present your work, create a Jupyter notebook ```cw2.ipynb``` that imports each of your python files completed above as modules and demonstrates their functionality by calling the indicated functions in separate cells within the notebook. The notebook should be formatted professionally using Markdown headings, including your name, a brief description of each section containing an exercise, and a brief description of each cell containing a solution demonstration. Check that exporting the notebook to html produces nice results that you would feel happy sharing with a colleague.

*Pro-tip:* Using `git` to manage conflicts with Jupyter notebooks can be a pain. I recommend delegating one person from your group to be the official notebook editor, to avoid merge conflicts later.

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

**CHANGEME**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**YOURNAME**
