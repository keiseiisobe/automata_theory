# First-Order Logic (FOL)

**First-Order Logic (FOL)**, also known as first-order predicate calculus or first-order predicate logic, is a formal system used in mathematics, philosophy, linguistics, and computer science to reason about objects, their properties, and their relationships [1, 2]. It is an extension of propositional logic, allowing for a much richer and more expressive way to represent and infer knowledge.

### Key Components of First-Order Logic:

Unlike propositional logic, which treats entire statements as atomic units, FOL delves into the internal structure of statements. Its main components are:

1.  **Terms**: These represent objects in the domain of discourse.
    *   **Constants**: Specific names for individual objects (e.g., `Socrates`, `5`, `Earth`).
    *   **Variables**: Placeholders for objects (e.g., `x`, `y`, `z`).
    *   **Functions**: Mappings from one or more objects to another object (e.g., `father_of(x)`, `plus(x, y)`, `successor(n)`).

2.  **Predicates (or Relations)**: These represent properties of objects or relationships between objects. They evaluate to true or false.
    *   **Unary Predicates**: Describe a property of a single object (e.g., `IsHuman(Socrates)`, `IsPrime(5)`).
    *   **Binary Predicates**: Describe a relationship between two objects (e.g., `Loves(John, Mary)`, `GreaterThan(5, 3)`).
    *   **N-ary Predicates**: For relationships involving 'n' objects.

3.  **Quantifiers**: These are the most distinctive feature of FOL, allowing statements about collections of objects.
    *   **Universal Quantifier ($\forall$)**: Means "for all" or "for every". (e.g., `∀x (IsHuman(x) → IsMortal(x))` - "For all x, if x is a human, then x is mortal").
    *   **Existential Quantifier ($\exists$)**: Means "there exists" or "for some". (e.g., `∃x (IsPrime(x) ∧ GreaterThan(x, 100))` - "There exists an x such that x is prime and x is greater than 100").

4.  **Logical Connectives**: Same as in propositional logic, used to combine statements:
    *   `¬` (NOT)
    *   `∧` (AND)
    *   `∨` (OR)
    *   `→` (IMPLIES)
    *   `↔` (IF AND ONLY IF)

5.  **Equality Symbol (=)**: Often included, allowing statements like `x = y`.

### Contrast with Propositional Logic:

The fundamental difference between propositional logic and first-order logic lies in their **expressive power** [1, 2]:

*   **Propositional Logic**: Deals with simple, atomic propositions (statements) that are either true or false. It focuses on how these propositions combine using logical connectives. It cannot analyze the internal structure of propositions or express general statements about objects.
    *   Example: `P → Q` ("If it is raining (P), then the ground is wet (Q)"). It cannot say "If *any* person is human, then *that same person* is mortal."

*   **First-Order Logic**: Can express more complex statements by referring to individual objects, their properties, and relationships, and by quantifying over them. This allows for reasoning about structured domains.
    *   Example: `∀x (IsHuman(x) → IsMortal(x))` ("All humans are mortal"). This statement explicitly links the property of being human to the property of being mortal for *every* individual `x`.

### Importance:

First-order logic is crucial because:
*   **Foundation for Mathematics**: It provides a powerful language for formalizing virtually all of mathematics, allowing for precise definitions of concepts and rigorous proofs [1].
*   **Artificial Intelligence and Knowledge Representation**: Used extensively in AI for knowledge representation, automated reasoning, and expert systems.
*   **Computer Science**: Foundational for database query languages (like SQL's underlying logic), program verification, and theoretical computer science (e.g., in defining formal languages and computability).
*   **Philosophy and Linguistics**: Used to analyze arguments and the structure of natural language.

**References:**
[1] Gamut, L. T. F. (1991). *Logic, Language, and Meaning, Volume 1: Introduction to Logic*. University of Chicago Press.
[2] Stanford Encyclopedia of Philosophy. "First-Order Model Theory" https://plato.stanford.edu/entries/model-theory/
[3] Mendelson, E. (1997). *Introduction to Mathematical Logic* (4th ed.). Chapman & Hall/CRC.
