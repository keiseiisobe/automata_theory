# Do You Love Coding?

![](BT_and_AT.png)

![](finite_state_machine_wiki.png)

# What is The Halting Problem?

![](halting_problem_wiki.png)

# Let's Prove the Halting Problem is Unsolvable

## Alan Turing's Proof by Contradiction (1936)

```python
def Q(P):
    # Step 1: Ask the H
	# "Does Program P halt on Input P?"
    answer = H(P, P)
	
	# Step 2: Do the Opposites
    if answer == "YES":
        Loop_Forever()
    else:
        Halt()
```

![](halting_problem.png)
