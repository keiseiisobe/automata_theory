# Relationship Diagram of Historical Foundations in Computability Theory

This diagram visualizes the key relationships and influences between the foundational concepts discussed in the `historical_foundations` directory.

```mermaid
graph TD
    A[Mathematical Paradoxes] --> B{Motivated}
    B --> C[Hilbert's Program]
    C --> D[Entscheidungsproblem]
    D -- "Addressed by" --> E[Halting Problem (Turing)]
    C -- "Undermined by" --> F[Gödel's Incompleteness Theorems]
    E -- "Demonstrates" --> G[Limits of Algorithmic Computation]
    F -- "Used in arguments by" --> H[Penrose's Arguments]
    G -- "Used in arguments by" --> H
    D -- "Answered negatively by" --> E
    C -- "Included Decidability as a goal" --> D
```