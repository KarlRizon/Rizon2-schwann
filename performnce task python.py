import turtle

# Create a turtle screen and turtle object
screen = turtle.Screen()
t = turtle.Turtle()

# Draw a star (5 points)
for _ in range(5):
    t.forward(100)  # Move forward by 100 units
    t.right(144)    # Turn right by 144 degrees

# Close the window on click
screen.exitonclick()
