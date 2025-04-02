Turtle 1:
This Python script uses the **Turtle** module to create and manipulate a turtle object that moves around on a graphical window. Let's break it down step by step:

---

### **Code Breakdown:**

1. **Initialize the Turtle Graphics Window:**
   ```python
   import turtle
   turtle.Screen()
   t = turtle.Pen()
   ```
   - The `turtle.Screen()` creates a window where the turtle will draw.
   - The `turtle.Pen()` initializes a turtle object named `t`.

2. **Move the Turtle:**
   ```python
   t.right(90)       # Rotate the turtle 90 degrees to the right (facing downward)
   t.forward(100)    # Move forward 100 units (downward since it rotated 90°)
   t.left(90)        # Rotate 90 degrees left (facing original direction)
   t.backward(100)   # Move backward 100 units (returns to the original position)
   ```
   - The turtle moves **down** first by 100 units, then **back** to the original position.

3. **Retrieve and Print Turtle's Information:**
   ```python
   print('The position is: ', t.pos())
   ```
   - Prints the current position of the turtle, which should be `(0,0)` since it moved back to its starting point.

   ```python
   print('Where are you towards North: ', t.towards(0,90))
   ```
   - `t.towards(0,90)` calculates the angle (in degrees) from the turtle’s current position to the point `(0,90)`.

   ```python
   print('The turtle x coordinate is: ', t.xcor())
   print('The turtle y coordinate is: ', t.ycor())
   ```
   - `t.xcor()` and `t.ycor()` return the turtle’s current x and y coordinates.

   ```python
   print('Turtle current heading: ', t.heading())
   ```
   - `t.heading()` gives the turtle’s current angle in degrees. After the movements, it should be `0` (facing the original direction).

   ```python
   print('Turtle is away by: ', t.distance(200,0))
   ```
   - `t.distance(200,0)` calculates the Euclidean distance between the turtle’s current position `(0,0)` and the point `(200,0)`. This should return `200`.

4. **End the Turtle Graphics Session:**
   ```python
   turtle.done()
   ```
   - Keeps the turtle graphics window open.

---

### **Expected Output:**
After running the script, the output in the console will be something like:

```
The position is:  (0.00,0.00)
Where are you towards North:  90.0
The turtle x coordinate is:  0.0
The turtle y coordinate is:  0.0
Turtle current heading:  0.0
Turtle is away by:  200.0
```

---

### **Summary of Actions:**
1. The turtle moves **down**, then **back up** to the original position.
2. The position remains `(0,0)`.
3. The `towards(0,90)` function calculates the direction from `(0,0)` to `(0,90)`, which is **90 degrees (North)**.
4. The distance to `(200,0)` is calculated as **200**.
5. The turtle's heading remains **0° (East/Right)**.

Turtle 2: 
This Python script uses the **Turtle** module to draw lines with different properties. Here's a step-by-step explanation of what it does:

---

### **Code Breakdown:**

1. **Initialize the Turtle Graphics Window:**
   ```python
   import turtle
   turtle.Screen()
   t = turtle.Pen()
   ```
   - Creates a drawing window.
   - Initializes a turtle object `t` to draw.

2. **First Line Drawing:**
   ```python
   t.forward(100)
   ```
   - Moves the turtle **100 units forward** while drawing a default black line.

3. **Lift the Pen and Move to a New Position:**
   ```python
   t.penup()
   t.goto(150, 100)
   ```
   - `t.penup()` lifts the pen so it won’t draw while moving.
   - `t.goto(150, 100)` moves the turtle to the new position `(150,100)` without drawing.

4. **Change Pen Properties:**
   ```python
   t.color('green')
   t.pensize(5)
   ```
   - Changes the drawing color to **green**.
   - Sets the pen thickness to **5 pixels**.

5. **Draw the Second Line:**
   ```python
   t.pendown()
   t.forward(100)
   ```
   - `t.pendown()` lowers the pen so it starts drawing again.
   - Moves forward **100 units**, drawing a thick **green** line.

6. **End the Turtle Session:**
   ```python
   turtle.done()
   ```
   - Keeps the turtle graphics window open.

---

### **Expected Output (Graphical):**
- A **black line** of default thickness (1px) starts from `(0,0)` and extends to `(100,0)`.
- The turtle **jumps** to `(150,100)` without drawing.
- A **thick green line** starts from `(150,100)` and extends forward **100 units**.

Turtle 3:
This Python script uses the **Turtle** module to manipulate the turtle's appearance. Here's a breakdown of what it does:

---

### **Code Breakdown:**

1. **Initialize the Turtle Graphics Window:**
   ```python
   import turtle
   turtle.Screen()
   t = turtle.Pen()
   ```
   - Creates a drawing window.
   - Initializes a turtle object `t`.

2. **Change Turtle Appearance:**
   ```python
   t.shape('turtle')
   ```
   - Sets the turtle’s shape to **a turtle icon** instead of the default arrow.

3. **Hide and Show the Turtle:**
   ```python
   t.hideturtle()
   ```
   - Hides the turtle (it won’t be visible in the window).
   ```python
   t.turtlesize(20)
   ```
   - Resizes the turtle to **20 times its original size**.
   ```python
   t.showturtle()
   ```
   - Makes the turtle visible again.

4. **Tilt the Turtle:**
   ```python
   t.settiltangle(-45)
   ```
   - Rotates (tilts) the turtle by **-45 degrees**.

5. **End the Turtle Session:**
   ```python
   turtle.done()
   ```
   - Keeps the turtle graphics window open.

---

### **Expected Output (Graphical):**
- A **large turtle-shaped cursor** appears on the screen.
- The turtle is **tilted at -45°**.
- The turtle **briefly disappears** (due to `hideturtle()`) before **reappearing larger**.

---

### **Notes:**
- `t.turtlesize(20)` makes the turtle **huge** and may not be entirely visible within the default window.
- `settiltangle(-45)` only works for certain shapes like "turtle," not for the default arrow shape.

Turtle Game:
This Python script implements a **simple turtle race game** using the **Turtle** and **Random** modules. Let's go through the code step by step.

---

## **Code Breakdown:**

### **1. Setup the Turtle Graphics Window**
```python
import turtle
import random

s = turtle.Screen()
s.bgcolor('red')
```
- The `turtle.Screen()` creates a graphical window.
- The background color is set to **red**.

---

### **2. Create Player Turtles**
```python
player_one = turtle.Pen()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
```
- `player_one` is a **green turtle**, positioned at `(-200, 100)`, ready to start.

```python
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)
```
- `player_two` is **a clone of player_one**, but colored **blue**.
- It starts at `(-200, -100)`.

---

### **3. Create Finish Line Circles**
```python
player_one.goto(300,80)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)

player_two.goto(300,-120)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)
```
- Each player has a **circle (finish line) at the end** of their path:
  - Player One’s finish line: `(300, 80)`
  - Player Two’s finish line: `(300, -120)`

---

### **4. Define the Dice (Die) Values**
```python
die = [1,2,3,4,5,6]
```
- A list representing a **six-sided die**.

---

### **5. Game Loop - Turtle Race**
```python
for i in range(20):
```
- The game runs for a maximum of **20 rounds** (but can end earlier if a player wins).

#### **Check for Winner**
```python
if player_one.pos() >= (300,100):
    print ("Player One Wins!")
    break
elif player_two.pos() >= (300,-100):
    print("Player Two Wins!")
    break
```
- If **either player reaches or exceeds** the finish line `(300,100)` or `(300,-100)`, the game announces the winner and **stops**.

#### **Player One's Turn**
```python
player_one_turn = input("Press 'Enter' to roll the die")
die_outcome = random.choice(die)
print("The result of the die roll is: ",die_outcome)
print("The number of steps will be: ",20*die_outcome)
player_one.fd(20*die_outcome)
player_one.stamp()
```
- The player presses **Enter** to roll the die.
- A **random number (1-6)** is chosen.
- The turtle moves forward **20 × die outcome** pixels.
- The turtle leaves a **stamp** (a footprint at its previous location).

#### **Player Two's Turn**
```python
player_two_turn = input("Press 'Enter' to roll the die")
die_outcome = random.choice(die)
print("The result of the die roll is: ",die_outcome)
print("The number of steps will be: ",20*die_outcome)
player_two.fd(20*die_outcome)
player_two.stamp()
```
- Similar to player one’s turn, but for player two.

---

### **6. Close the Turtle Window on Click**
```python
turtle.exitonclick()
```
- The window remains open until the user clicks to close it.

---

## **How the Game Works**
1. **Two turtles (green and blue) start at `(-200,100)` and `(-200,-100)`.**
2. **They take turns rolling a die (1-6).**
3. **Each die roll moves the turtle forward by `20 × die outcome` pixels.**
4. **The first turtle to reach its finish line wins.**
5. **Players press Enter to roll the die for each turn.**
6. **The game stops as soon as one player wins.**
7. **The screen closes when clicked.**

---

### **Possible Enhancements**
- **Automate die rolls** instead of requiring user input.
- **Add a countdown timer** before each player's turn.
- **Include a start button** instead of an immediate game start.
- **Play sound effects** when the turtle moves.
- **Draw a track** for each turtle to follow.

Turtle Guide:
This Python script uses the **Turtle** module to create a graphical window and draw a filled **equilateral triangle** with some additional visual effects. Let's break it down step by step.

---

## **Code Breakdown:**

### **1. Setup the Turtle Graphics Window**
```python
import turtle

s = turtle.Screen()
s.bgcolor('green')  
s.title("Python Guide")
```
- Creates a drawing window.
- Sets the **background color to green**.
- Sets the **title of the window to "Python Guide"**.

---

### **2. Create and Customize the Turtle**
```python
t = turtle.Pen()
```
- Creates a turtle object `t` for drawing.

```python
t.shapesize(10,5,1)
t.color("blue", "red")
```
- **Shapesize (10,5,1)**:
  - **Stretch factor:** Increases the size of the turtle's shape.
  - **Width:** 10 times normal.
  - **Height:** 5 times normal.
  - **Outline width:** 1.
- **Color ("blue", "red")**:
  - **Blue** is the **pen (outline) color**.
  - **Red** is the **fill color**.

```python
t.shape("arrow")
t.speed(2)
```
- Changes the turtle **shape to an arrow**.
- Sets **speed to 2** (moderate speed).

---

### **3. Draw a Filled Equilateral Triangle**
```python
t.begin_fill()
```
- Starts **filling the shape** with the specified **red** color.

#### **First Side**
```python
t.fd(300)   # Move forward by 300 units
t.lt(120)   # Turn left by 120 degrees
t.stamp()   # Leaves a turtle-shaped stamp at the current position
```
- Draws the **first side** of the triangle.
- Leaves a **stamp** (a visual marker at this point).

#### **Second Side**
```python
t.fd(300)
t.lt(120)
t.stamp()
```
- Draws the **second side**.
- Leaves another **stamp**.

#### **Third Side**
```python
t.fd(300)
t.lt(120)
```
- Draws the **third side**, closing the triangle.

```python
t.end_fill()
```
- **Fills** the triangle with the **red** color.

---

### **4. Keep the Window Open**
```python
turtle.done()
```
- Keeps the Turtle graphics window **open**.

---

## **Expected Output (Graphical)**
- A **red equilateral triangle** outlined in **blue**.
- The turtle **stamps** at each corner of the triangle.
- The background is **green**.
- The turtle starts as an **arrow shape** but stretches in size.

---

## **Possible Enhancements**
- **Change the shape** to `"turtle"` instead of `"arrow"`.
- **Increase speed** (`t.speed(10)`) for faster drawing.
- **Use random colors** for each side using `random.choice()`.
- **Draw multiple shapes** in different colors.
- **Animate the turtle moving** around the triangle.
