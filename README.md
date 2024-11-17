# programming_formalisms_project_autumn_2024

[![Check links](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2024/actions/workflows/check_links.yaml/badge.svg)](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2024/actions/workflows/check_links.yaml)
[![Check package](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2024/actions/workflows/check_package.yaml/badge.svg)](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2024/actions/workflows/check_package.yaml)
[![Check spelling](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2024/actions/workflows/check_spelling.yaml/badge.svg)](https://github.com/programming-formalisms/programming_formalisms_project_autumn_2024/actions/workflows/check_spelling.yaml)


Learners' project of the Programming Formalisms course of autumn 2024.

## Goal

To simulate bacterial movement in 2D space.

One way to model bacterial movement is 
the run and tumble model,
where 'run' is going straight in a direction,
and 'tumble' is picking a random direction.
The 'run' lasts longer when a bacterium
finds more and more nutrients (e.g. dissolved
sugars), and lasts shorter
when finding less and less nutrients.

![](run_and_tumble.jpg)

> Image from [coursehero](https://www.coursehero.com/study-guides/microbiology/unique-characteristics-of-prokaryotic-cells/)

## Project state

This will change over the course's time.

Parameter                |Value
-------------------------|-----------------------
Branching setup          |Trunk-based development
Merge workflow           |Not applicable
Testing                  |None
Continuous integration   |None
Can be used as a package?|No

## Team roles

Role              |Name
------------------|-----------------------
Product owner     |.
Software architect|.
Data manager      |.
Lead developer    |.

## Usage

> The lead developer and product owner are free to change this,
> if they both agree on the new usage.

```python
from bacsim.simulation import run_experiment
run_experiment("parameters.csv", "results.csv")
```

## Internal links

 * [design](design/README.md): design documents
 * [learners](learners/README.md): place to keep notes and do exercises on an individual basis

## External links

 * [Programming Formalisms GitHub repository](https://github.com/UPPMAX/programming_formalisms)

## References

 * [Wang et al., 2011] Wang, Charles CN, et al. "Simulation of bacterial chemotaxis by the random run and tumble model." 2011 IEEE 11th International Conference on Bioinformatics and Bioengineering. IEEE, 2011.
