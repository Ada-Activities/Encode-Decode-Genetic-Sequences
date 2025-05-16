# Class Activity - Debugging Dahlia’s Project with ChatGPT

## Overview 

We helped fix Dahlia's code in the Debugging Continued lesson's Problem Set, so we should have an idea of where the bugs are in this starter code and how to fix them. This puts us in a great position to try out debugging with ChatGPT using known issues, allowing us to focus on strategies for prompting rather than finding the bugs.

As a reminder, `main.py` holds the driving code while `source/part_one.py` and `source/part_two.py` contain the functions for working with the genetic sequences as strings. The `tests` folder holds files with tests for both Part 1 and Part 2 of the problem set.

## Part 1

### Before Getting Started:

We want to run Dahlia's code and see the same issues, in the same order, as we saw when debugging the problem set. As a group choose someone's existing local repository to use. 

**You may need to revert some changes:**
1. Any code changes made to fix the bugs
2. In `main.py` at the top of the file:
   - comment out the part 2 import statement `from part_two import driver`
   - uncomment the part 1 import line `# from part_one import driver`

### Writing Prompts for Debugging

This activity is mostly discussion-based. We will be working in groups to write prompts together to explain errors and help pinpoint issues while practicing validating ChatGPT’s responses. The goals for today are to get hands on experience writing prompts for debugging while sharing and incorporating each other's perspectives on:
- What information could be helpful in a prompt 
- How to explain any errors received
- How to explain expected behavior vs. observed code behaviors to people or ChatGPT 
- How to select what code to share with ChatGPT for context
- How to evalute ChatGPT’s responses for correctness and usefulness

### Potential Workflow

If you’d like some direction getting started, feel free to use the flow below:
1. Run the code from the terminal using `python3 main.py`. Look at the error Dahlia’s receiving. Discuss as a group what info it’s giving you, then do a web search for the error to see what kind of information surfaces.
2. Next, discuss the questions 1-4 listed above as a group. Use the answers to the questions to organize a prompt as a group asking ChatGPT to explain what is happening in the code. 
3. Discuss together what was or was not useful about the response. If the group tried multiple versions, also discuss which prompts helped most.  
4. ChatGPT might already try to suggest fixes to the bug in the first response. If it has not, using your team's knowledge of the bugs from the problem set, write up a prompt for ChatGPT that shares the code and asks for assistance debugging the error. Feel free to iterate on the prompt and share more or less code to see how it affects the response. 
5. Decide as a team how to use the information from ChatGPT, and how you might want to fix the issue. Apply your changes, and run the tests!
6. Follow this pattern for further bugs you find.

## Part 2

### Before Getting Started:

In `main.py` at the top of the file:
- comment out the part 1 import statement `from part_one import driver`
- uncomment the part 2 import line `# from part_two import driver`

### Debugging Refactored Code

Dahlia refactored her code in `part_two.py`, but found a new issue when categorizing the strings. 
1. Debug the issue with your team using the techniques you practiced in part 1. 
2. Discuss as a team how you could write a prompt to ask for help refactoring the fixed part 1 code to be more efficient. Share it with ChatGPT and discuss the result. 
   - Did ChatGPT come up with the same optimization as Dahlia?
   - Are there other helpful or unhelpful changes ChatGPT suggested?
   - How might you want to adjust the prompt if you had more time?