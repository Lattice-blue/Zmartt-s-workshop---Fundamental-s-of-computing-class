### I. The Core Concept: What is a "Root"?

A **root** (or **zero**) of a function $f(x)$ is simply any value of $x$ that makes the function evaluate to **zero**:

$$f(x) = 0$$

```
               y
               │          Curve: y = f(x)
               │             /
  Positive (+) │            / 
───────────────┼───────────●───────────────> x
  Negative (-) │          /  (THE ROOT: f(x) = 0, y crosses the axis)
               │         /
               │        /
```

* **Geometrically:** A root is the exact horizontal coordinate where the graph of $y = f(x)$ **crosses or touches the $x$-axis** (where altitude $y = 0$).

---

### II. Why Do Numerical Methods Exist? (Analytical vs. Numerical)

Look at your image:
* **Analytical Method (Exact Algebra):** You take $x^2 + 3x - 10 = 0$, factor it into $(x + 5)(x - 2) = 0$, and find $x = -5, 2$. 

**The Problem:** In the 1820s, mathematicians Niels Henrik Abel and Évariste Galois proved the **Abel-Ruffini Theorem**:
> There is **no general algebraic formula** (like the quadratic formula) to solve polynomials of degree 5 or higher (e.g., $x^5 - 5x + 1 = 0$), or equations mixing algebra and trigonometry (e.g., $x = \cos(x)$).

Because exact algebraic formulas physically do not exist for most equations, computers must use **Numerical Methods**: algorithms that start with an initial guess and iteratively march closer and closer to the root until the error is smaller than a chosen threshold (e.g., $\text{error} < 0.0001$).

---

### III. The Three Root-Finding Engines

```
┌───────────────────────────┬───────────────────────────┬───────────────────────────┐
│ 1. BISECTION METHOD       │ 2. NEWTON-RAPHSON METHOD  │ 3. SECANT METHOD          │
│ (The Safe Squeeze)        │ (The Tangent Rocket)      │ (The Derivative-Free Line)│
├───────────────────────────┼───────────────────────────┼───────────────────────────┤
│ Guarantees convergence    │ Extremely fast            │ Fast                      │
│ Slow (Linear)             │ Requires derivative f'(x) │ No derivative required    │
│ Needs [a, b] bracket      │ Needs 1 starting guess    │ Needs 2 starting guesses  │
└───────────────────────────┴───────────────────────────┴───────────────────────────┘
```

---

### 1. The Bisection Method (The Safe Squeeze)

#### Jargon Deconstructed:
* **"Continuous Function":** A curve you can draw without lifting your pen from the paper (no vertical breaks, jumps, or holes).
* **"Intermediate Value Theorem (IVT)":** If you are below sea level at point $a$ ($f(a) < 0$) and above sea level at point $b$ ($f(b) > 0$), and the path is unbroken, **you must have crossed sea level ($f(x) = 0$) at least once between $a$ and $b$.**
* **"Bracketing":** Finding two boundary points $a$ and $b$ whose outputs have **opposite signs** ($f(a) \cdot f(b) < 0$).

```
        f(b) is (+)  ──>                       ● (b, f(b))
                                              /
────────────────────────────[  Midpoint m  ]─/──────────> x
                           /       │        /
  (a, f(a)) ● <── f(a) is (-)      │       /
                                   ▼
                       Check sign of f(m):
                       If f(m) is (-), new bracket is [m, b]
                       If f(m) is (+), new bracket is [a, m]
```

#### The Mental Model:
1. Start with an interval $[a, b]$ where $f(a)$ and $f(b)$ have opposite signs ($f(a) \cdot f(b) < 0$).
2. Compute the exact middle point: $m = \frac{a + b}{2}$.
3. Check $f(m)$:
   * If $f(m) = 0$ (or is within tolerance): $m$ is your root.
   * If $f(m)$ has the same sign as $f(a)$: the root is in the right half $\implies$ set $a = m$.
   * If $f(m)$ has the same sign as $f(b)$: the root is in the left half $\implies$ set $b = m$.
4. **Result:** Every step cuts the search space in half (exactly like binary search). It is mathematically impossible for Bisection to fail if the initial bracket is valid, but it is slow.

---

### 2. The Newton-Raphson Method (The Tangent Rocket)

#### Jargon Deconstructed:
* **"Derivative $f'(x)$":** The exact slope (steepness) of the curve at a specific point $x$.
* **"Tangent Line":** The straight line that grazes the curve at a single point, matching its exact slope.

```
                   Curve y = f(x)
                        /
                       ● (x_0, f(x_0))
                      / ╲
                     /   ╲  Tangent line with slope f'(x_0)
                    /     ╲
───────────────────/───────●──────────────────> x
                  /       x_1 (Where tangent hits the x-axis)
                 /
```

#### The Mental Model:
Instead of blindly cutting an interval in half, you use calculus to make an educated leap:
1. Stand at an initial guess $x_0$.
2. Calculate the height $f(x_0)$ and the slope $f'(x_0)$.
3. Draw a straight tangent line down that slope until it hits the ground ($y = 0$).
4. The point where the tangent hits the ground becomes your next, much better guess $x_1$.

#### The Derivation (Point-Slope Form):
Equation of the tangent line:
$$y - f(x_0) = f'(x_0)(x - x_0)$$

We want to find where the line hits the ground ($y = 0$ at new point $x_1$):
$$0 - f(x_0) = f'(x_0)(x_1 - x_0)$$
$$-f(x_0) = f'(x_0)(x_1 - x_0)$$
$$x_1 - x_0 = -\frac{f(x_0)}{f'(x_0)}$$

$$\mathbf{x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}}$$

* **Speed:** Extremely fast (quadratic convergence). The number of accurate decimal places roughly **doubles with every iteration**.
* **Vulnerability:** If the slope is flat ($f'(x) \approx 0$), division by zero launches your guess to infinity.

---

### 3. The Secant Method (The Practical Approximation)

#### Jargon Deconstructed:
* **"Secant Line":** A straight line drawn through **two distinct points** on a curve.

#### The Mental Model:
What if the derivative $f'(x)$ is impossible or too complicated to calculate by hand?
* You approximate the slope $f'(x)$ using the slope between your **two most recent guesses**, $x_0$ and $x_1$:

$$\text{Slope } \approx \frac{f(x_1) - f(x_0)}{x_1 - x_0}$$

* Substitute this slope approximation directly into Newton's formula:

$$\mathbf{x_{n+1} = x_n - f(x_n) \cdot \left[ \frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})} \right]}$$

* **Advantage:** You do not need calculus or derivatives ($f'(x)$). You only need the original function $f(x)$.
* **Requirement:** It requires **two initial guesses** ($x_0, x_1$) to draw the first line.

---

### Summary Checklist

| Method | Initial Inputs Needed | Mathematical Engine | Safety Profile |
| :--- | :--- | :--- | :--- |
| **Bisection** | Interval $[a, b]$ where $f(a)\cdot f(b) < 0$ | Intermediate Value Theorem (Halving) | 100% Reliable, Slow |
| **Newton-Raphson** | 1 Guess $x_0$ + Derivative $f'(x)$ | Tangent line slope projection | Blazingly Fast, Fragile near flat slopes |
| **Secant** | 2 Guesses $x_0, x_1$ (No derivative) | Secant line slope approximation | Fast, No calculus needed |

State which method you want to trace with a concrete numerical step first.