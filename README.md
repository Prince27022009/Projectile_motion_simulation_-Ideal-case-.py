# Projectile_motion_simulation_-Ideal-case-.py


## ⭐ Projectile Motion Visualizer (Ideal Physics Model)

This project is a clean and full visual simulation of ideal projectile motion. It calculates everything using direct physics formulas, and plots the entire trajectory with automatic scaling, markers, arrows, and important visual guides. 
I built this over 3 days while balancing academics, using AI assistance mainly for debugging, structuring, and polishing the final implementation.



## 🔍 What This Project Does

•Plots the full trajectory of a projectile using ideal kinematic equations

•Shows maximum height, range, time of flight and final velocity directly on the graph

•Marks the start, peak, and landing points

•Draws direction arrows along the curve

•Adds dashed lines to clearly show the peak height and its vertical alignment

•Auto-scales the entire graph based on the input parameters


•Runs smoothly on Turtle without installing any external libraries


•Everything is visual, accurate, and easy to understand.



## 🧠 How It Works

This simulator uses closed-form physics equations:

•**x(t) = v0 * cos(θ) * t**

•**y(t) = v0 * sin(θ) * t - 0.5 * g * t²**

•**T = (2 * v0 * sin(θ)) / g**

•**H = (v0² * sin²(θ)) / (2g)**

•**R = (v0² * sin(2θ)) / g**


Using 200 sample points gives a smooth trajectory when plotted with Turtle.
No numerical integration, no drag model, and no frame-by-frame animation — just pure, ideal motion.



## 🎯 Features

•Ideal projectile model

•Smooth 200-point trajectory

•Auto scaling

•Direction arrows to show the motion

•Clean annotations

•Dashed horizontal & vertical guides

•Final velocity vector and speed

•Constant acceleration display


This project aims to stay simple, understandable, and fast while still looking polished.



## 🧩 Why I Built This

I wanted to create something that shows real physics visually without relying on heavy libraries like matplotlib. The idea was to build a project that actually looks good, fits within high school basic kinametics, and still feels meaningful. It also helped me practice structuring code, working with turtle graphics, applying formulas correctly, and using AI as a tool, not a crutch.



## 🤖 AI Assistance Disclaimer

I designed the logic, physics flow, visual layout, and overall structure myself.
AI was used for:

•**debugging**

•**checking formulas**

•**improving structure**

•**polishing the final version**


The core idea, execution, and decisions are mine.



## 🚀 How to Run

Just run the Python file. No installations are needed.

**Example:**
•INPUT
–> initial speed = 40 m/s
–> launch angle = 45°

• OUTPUT
![Example Output](Output_screenshot)
