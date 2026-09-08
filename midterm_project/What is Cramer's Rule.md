### I. The Origin: Solving by Plain Elimination

Forget determinants and matrices for a moment. Look at a standard system of two linear equations with two unknowns ($x$ and $y$):

$$\begin{cases} (1) \quad a_1 x + b_1 y = c_1 \\ (2) \quad a_2 x + b_2 y = c_2 \end{cases}$$

Here, $a_1, a_2, b_1, b_2, c_1, c_2$ are just known numbers (like $2, 3, 5$). We want to solve for $x$ and $y$.

---

#### Step 1: Eliminate $y$ to solve for $x$
To cancel out $y$, multiply Equation (1) by $b_2$, and multiply Equation (2) by $b_1$:

$$b_2(a_1 x + b_1 y) = b_2(c_1) \implies \mathbf{a_1 b_2}x + b_1 b_2 y = \mathbf{c_1 b_2}$$
$$b_1(a_2 x + b_2 y) = b_1(c_2) \implies \mathbf{a_2 b_1}x + b_1 b_2 y = \mathbf{c_2 b_1}$$

Now, subtract the second equation from the first:
$$(a_1 b_2 - a_2 b_1)x + (b_1 b_2 y - b_1 b_2 y) = c_1 b_2 - c_2 b_1$$
$$(a_1 b_2 - a_2 b_1)x = c_1 b_2 - c_2 b_1$$

Divide both sides to isolate $x$:
$$\mathbf{x = \frac{c_1 b_2 - c_2 b_1}{a_1 b_2 - a_2 b_1}}$$

---

#### Step 2: Eliminate $x$ to solve for $y$
Do the exact same thing, but eliminate $x$. Multiply Equation (1) by $a_2$ and Equation (2) by $a_1$:

$$a_2(a_1 x + b_1 y) = a_2(c_1) \implies a_1 a_2 x + \mathbf{a_2 b_1}y = a_2 c_1$$
$$a_1(a_2 x + b_2 y) = a_1(c_2) \implies a_1 a_2 x + \mathbf{a_1 b_2}y = a_1 c_2$$

Subtract the first from the second:
$$(a_1 b_2 - a_2 b_1)y = a_1 c_2 - a_2 c_1$$

Divide to isolate $y$:
$$\mathbf{y = \frac{a_1 c_2 - a_2 c_1}{a_1 b_2 - a_2 b_1}}$$

---

### II. The Pattern Discovery

Look closely at the formulas for $x$ and $y$:

$$x = \frac{\mathbf{c_1 b_2 - c_2 b_1}}{\mathbf{a_1 b_2 - a_2 b_1}}, \qquad y = \frac{\mathbf{a_1 c_2 - a_2 c_1}}{\mathbf{a_1 b_2 - a_2 b_1}}$$

Notice three structural patterns:
1. **The Denominators are IDENTICAL:** Both fractions are divided by the exact same expression:
   $$D = a_1 b_2 - a_2 b_1$$
2. **The Numerator for $x$ ($D_x$):** Look at $c_1 b_2 - c_2 b_1$. It is the exact same structure as $D$, except the $a$-coefficients ($a_1, a_2$) were replaced by the constants ($c_1, c_2$).
3. **The Numerator for $y$ ($D_y$):** Look at $a_1 c_2 - a_2 c_1$. It is the exact same structure as $D$, except the $b$-coefficients ($b_1, b_2$) were replaced by the constants ($c_1, c_2$).

---

### III. Inventing the "Determinant" as a Shorthand

Mathematicians saw that this cross-multiplication pattern:
$$\text{Top-Left} \times \text{Bottom-Right} \;-\; \text{Top-Right} \times \text{Bottom-Left}$$
keeps showing up everywhere in algebra. 

So they invented a compact notation for it called a **$2 \times 2$ Determinant**:

$$\begin{vmatrix} p & q \\ r & s \end{vmatrix} \equiv p\cdot s - q\cdot r$$

```
   p ───╲───> s     (+) (Multiply main diagonal: p * s)
         ╲   
   r ───╱───> q     (-) (Subtract other diagonal: q * r)
```

---

### IV. Cramer's Rule: Putting It Together

Using this new box notation, the elimination results become visual:

1. **The Main Determinant ($D$):** Put all the coefficients of $x$ and $y$ into the box:
   $$D = \begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix} = a_1 b_2 - b_1 a_2$$

2. **The $x$-Determinant ($D_x$):** Replace the $x$-column with the answer column $\begin{bmatrix} c_1 \\ c_2 \end{bmatrix}$:
   $$D_x = \begin{vmatrix} \mathbf{c_1} & b_1 \\ \mathbf{c_2} & b_2 \end{vmatrix} = c_1 b_2 - b_1 c_2$$

3. **The $y$-Determinant ($D_y$):** Replace the $y$-column with the answer column $\begin{bmatrix} c_1 \\ c_2 \end{bmatrix}$:
   $$D_y = \begin{vmatrix} a_1 & \mathbf{c_1} \\ a_2 & \mathbf{c_2} \end{vmatrix} = a_1 c_2 - c_1 a_2$$

Then **Cramer's Rule** is simply:

$$x = \frac{D_x}{D} \quad \text{and} \quad y = \frac{D_y}{D}$$

---

### V. A Concrete Numerical Example

Solve this system using the rule:
$$\begin{cases} 2x + 3y = 8 \\ 1x + 4y = 9 \end{cases}$$

1. **Calculate $D$ (from the left-hand coefficients):**
   $$D = \begin{vmatrix} 2 & 3 \\ 1 & 4 \end{vmatrix} = (2 \cdot 4) - (3 \cdot 1) = 8 - 3 = \mathbf{5}$$

2. **Calculate $D_x$ (swap first column with $\begin{bmatrix} 8 \\ 9 \end{bmatrix}$):**
   $$D_x = \begin{vmatrix} \mathbf{8} & 3 \\ \mathbf{9} & 4 \end{vmatrix} = (8 \cdot 4) - (3 \cdot 9) = 32 - 27 = \mathbf{5}$$

3. **Calculate $D_y$ (swap second column with $\begin{bmatrix} 8 \\ 9 \end{bmatrix}$):**
   $$D_y = \begin{vmatrix} 2 & \mathbf{8} \\ 1 & \mathbf{9} \end{vmatrix} = (2 \cdot 9) - (8 \cdot 1) = 18 - 8 = \mathbf{10}$$

4. **Apply Cramer's Rule:**
   $$x = \frac{D_x}{D} = \frac{5}{5} = \mathbf{1}$$
   $$y = \frac{D_y}{D} = \frac{10}{5} = \mathbf{2}$$

---

### VI. The Only Failure Mode: Division by Zero ($D = 0$)

Look at the formulas: $x = \frac{D_x}{D}$ and $y = \frac{D_y}{D}$.

* If **$D = 0$**, division by zero is undefined.
* Geometrically, $D = 0$ means the two lines are **parallel** (they never cross $\implies$ No solution) or they are the **same line** (infinitely many solutions).
* Cramer's Rule only works when **$D \neq 0$**.

Does this algebraic derivation make the pattern clear?