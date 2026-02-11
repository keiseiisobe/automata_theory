# State Machines

A **state machine**, also known as a finite-state machine (FSM), is a mathematical model of computation used to design and analyze systems that behave differently depending on their history or current mode of operation [1]. It's the simplest form of abstract machine in automata theory and serves as a fundamental building block for understanding more complex computational models.

## Core Components:

A state machine is defined by a set of core components:

1.  **States (Q)**: A finite set of possible configurations or modes that the machine can be in. At any given moment, the machine is in exactly one state.
    *   *Example*: A traffic light can be in `Red`, `Yellow`, or `Green` states.

2.  **Input Alphabet ($\Sigma$)**: A finite set of possible input symbols or events that the machine can receive.
    *   *Example*: For a traffic light, inputs might be `TimerExpires` or `PedestrianButtonPress`.

3.  **Transition Function ($\delta$)**: A rule that specifies how the machine changes from one state to another based on the current state and the received input. It maps a (current state, input) pair to a next state.
    *   *Example*: From `Green` state, on `TimerExpires` input, transition to `Yellow`.

4.  **Initial State ($q_0$)**: The state in which the machine begins operation.
    *   *Example*: A traffic light might always start in the `Red` state when powered on.

5.  **Output Function (Optional, for Mealy/Moore Machines)**: Some state machines produce outputs.
    *   *Mealy Machine*: Output depends on both the current state and the input.
    *   *Moore Machine*: Output depends only on the current state.

6.  **Accept States (F) (Optional, for Recognizers/Acceptors)**: A subset of states that indicate a successful completion or recognition of a pattern. If the machine ends in an accept state after processing an input sequence, the sequence is "accepted."

## Types of Finite-State Machines:

*   **Deterministic Finite Automaton (DFA)**: For each state and each input symbol, there is exactly one transition to a next state.
*   **Non-deterministic Finite Automaton (NFA)**: For each state and input symbol, there can be zero, one, or multiple transitions to next states. NFAs can also have $\epsilon$-transitions (transitions without consuming an input symbol). It has been proven that NFAs and DFAs have equivalent power in terms of the languages they can recognize [2].
*   **Mealy Machine**: Outputs are associated with transitions.
*   **Moore Machine**: Outputs are associated with states.

## Simple Examples:

### 1. Light Switch

*   **States**: `On`, `Off`
*   **Input**: `Press`
*   **Transition**: If `Off` and `Press`, go to `On`. If `On` and `Press`, go to `Off`.
*   **Output**: The light being lit or not.

### 2. Turnstile

*   **States**: `Locked`, `Unlocked`
*   **Inputs**: `Coin`, `Push`
*   **Transitions**:
    *   From `Locked`, on `Coin`, go to `Unlocked`.
    *   From `Unlocked`, on `Push`, go to `Locked`.
    *   Other inputs from `Locked` (e.g., `Push`) have no effect, or stay in `Locked`. Other inputs from `Unlocked` (e.g., `Coin`) have no effect, or stay in `Unlocked`.
*   **Outputs**: From `Locked` on `Coin`, output `Thank You`. From `Unlocked` on `Push`, output `Person Passed`.

## Applications:

State machines are incredibly versatile and have numerous practical applications across computer science and engineering [1, 3]:

*   **Digital Circuit Design**: Used to design sequential logic circuits (e.g., controllers for CPUs, vending machines).
*   **Lexical Analysis in Compilers**: Finite automata are used to recognize tokens (keywords, identifiers, numbers) in programming language source code.
*   **Protocol Design**: Modeling communication protocols (e.g., TCP connection states, network handshakes).
*   **User Interface Design**: Modeling user interactions and application states (e.g., a button's states: normal, hovered, pressed).
*   **Game AI**: Designing simple AI behaviors for non-player characters.
*   **Text Processing/Pattern Matching**: Regular expressions, which are recognized by finite automata, are widely used for pattern matching in text.

## Connection to Automata Theory:

State machines, particularly finite automata, represent the lowest level of computational power in the **Chomsky Hierarchy** [4]. They are capable of recognizing **regular languages**, which are languages that can be described by regular expressions. Understanding state machines is the first step in understanding the theoretical limits and capabilities of different computational models.

**References:**
[1] Hopcroft, J. E., Motwani, R., & Ullman, J. D. (2006). *Introduction to Automata Theory, Languages, and Computation* (3rd ed.). Pearson Addison-Wesley.
[2] Sipser, M. (2012). *Introduction to the Theory of Computation* (3rd ed.). Cengage Learning. (Provides detailed definitions of DFAs and NFAs).
[3] Wikipedia. "Finite-state machine". https://en.wikipedia.org/wiki/Finite-state_machine
[4] Chomsky, N. (1956). Three models for the description of language. *IRE Transactions on Information Theory*, 2(3), 113-124.
