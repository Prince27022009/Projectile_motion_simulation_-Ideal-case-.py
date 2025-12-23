import math
import turtle

gravity = 9.8


# SETUP SCREEN


screen = turtle.Screen()
screen.title("Projectile Motion - Annotated Trajectory (Ideal Motion)")
screen.bgcolor("black")
screen.setup(width=900, height=600)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.width(2)
pen.color("cyan")


# USER INPUT


v0 = float(turtle.numinput("Velocity", "Initial speed (m/s):", 40))
angle = float(turtle.numinput("Angle", "Launch angle (degrees):", 45))

angle = math.radians(angle)


# ANALYTIC PHYSICS (Ideal Projectile Motion)


# Time of flight
T = (2 * v0 * math.sin(angle)) / gravity

# Maximum height
H = (v0**2 * (math.sin(angle))**2) / (2 * gravity)

# Range
R = (v0**2 * math.sin(2 * angle)) / gravity

# Peak occurs at:
t_peak = T / 2
x_peak = v0 * math.cos(angle) * t_peak


# GENERATE TRAJECTORY POINTS


xs = []
ys = []

num_points = 200  # smooth curve
for i in range(num_points + 1):
    t = (i / num_points) * T
    x = v0 * math.cos(angle) * t
    y = v0 * math.sin(angle) * t - 0.5 * gravity * t**2
    xs.append(x)
    ys.append(max(y, 0))  # ensure ground cutoff


# AUTO-SCALING
scale_x = 800 / (R + 1)
scale_y = 500 / (H + 1)
SCALE = min(scale_x, scale_y)

def sx(x): return -400 + x * SCALE
def sy(y): return y * SCALE


# DRAW AXES


def draw_axes():
    axis = turtle.Turtle()
    axis.hideturtle()
    axis.color("white")
    axis.speed(0)

    # X-axis
    axis.penup()
    axis.goto(-420, 0)
    axis.pendown()
    axis.goto(420, 0)

    # Y-axis
    axis.penup()
    axis.goto(0, -280)
    axis.pendown()
    axis.goto(0, 280)

draw_axes()


# DRAW TRAJECTORY CURVE


pen.penup()
pen.goto(sx(xs[0]), sy(ys[0]))
pen.pendown()

for i in range(len(xs)):
    pen.goto(sx(xs[i]), sy(ys[i]))


# MARKERS + LABELS


marker = turtle.Turtle()
marker.hideturtle()
marker.penup()
marker.color("white")

# Start point
marker.goto(sx(0), sy(0))
marker.dot(10, "blue")
marker.goto(sx(0) + 10, sy(0) - 15)
marker.write("Start", font=("Arial", 10, "normal"))

# Peak point
marker.goto(sx(x_peak), sy(H))
marker.dot(12, "red")
marker.goto(sx(x_peak) + 10, sy(H) + 10)
marker.write("Maximum Height", font=("Arial", 10, "normal"))

# Landing point (Range)
marker.goto(sx(R), 0)
marker.dot(12, "yellow")
marker.goto(sx(R) - 50, -20)
marker.write("Landing / Range", font=("Arial", 10, "normal"))


# DASHED MAX HEIGHT LINE


dash = turtle.Turtle()
dash.hideturtle()
dash.color("gray")
dash.speed(0)

y_line = sy(H)

for x in range(-380, int(sx(R)) + 1, 20):
    dash.penup()
    dash.goto(x, y_line)
    dash.pendown()
    dash.goto(x + 10, y_line)
    
    
# VERTICAL DASHED LINE AT PEAK
for y in range(int(sy(H)), 0, -15):
    dash.penup()
    dash.goto(sx(x_peak), y)
    dash.pendown()
    dash.goto(sx(x_peak), y - 8)


# CALCULATE FINAL VELOCITY 
vx_final = v0 * math.cos(angle)
vy_final = -v0 * math.sin(angle)
v_final = math.sqrt(vx_final**2 + vy_final**2)



# DISPLAY STATS BOX
text = turtle.Turtle()
text.hideturtle()
text.color("white")
text.penup()
text.goto(-380, 240)
text.write(
    f"Max Height: {H:.2f} m\n"
    f"Range: {R:.2f} m\n"
    f"Flight Time: {T:.2f} s\n\n"
    f"Final Velocity (Vx, Vy): ({vx_final:.2f}, {vy_final:.2f}) m/s\n"
    f"Final Speed: {v_final:.2f} m/s\n",
    font=("Arial", 12, "normal")
)

turtle.done()
