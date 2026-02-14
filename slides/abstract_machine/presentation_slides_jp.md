<img src="I_love_coding.jpg" width="500px">

![](BT_and_AT.png)

![](finite_state_machine_wiki.png)

![](halting_problem_wiki_jp.png)

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
