from manim import *
import numpy as np

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30

class SuperellipseCurveSweep(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Superellipse", color=WHITE, weight=BOLD).scale(1.2)
        title.move_to(UP * 3.5)

        formula = MathTex(
            r"\left|\frac{x}{a}\right|^r + \left|\frac{y}{b}\right|^r - 1 = 0",
            color=YELLOW
        ).scale(0.75)
        formula.next_to(title, DOWN, buff=0.5)

        param_label = MathTex("r = 0.00", color=YELLOW).scale(0.8)
        param_label.next_to(formula, DOWN, buff=0.3)

        self.play(Write(title), Write(formula), Write(param_label))

        axes = Axes(
            x_range=[-1.5, 1.5],
            y_range=[-1.5, 1.5],
            x_length=6,
            y_length=6,
            axis_config={"color": GRAY}
        ).move_to(DOWN * 2.5)
        self.play(Create(axes))

        colors = [BLUE, TEAL, GREEN, YELLOW, ORANGE, RED]
        r_values = np.linspace(0.5, 5.0, len(colors))
        a, b = 1, 1

        for i, r in enumerate(r_values):
            new_param = MathTex(f"r = {r:.2f}", color=YELLOW).scale(0.8)
            new_param.move_to(param_label.get_center())

            def superellipse_fn(x, y):
                return (np.abs(x / a))**r + (np.abs(y / b))**r - 1

            curve = axes.plot_implicit_curve(
                superellipse_fn,
                color=colors[i],
                stroke_width=2,
                min_depth=0.01
            )

            self.play(Transform(param_label, new_param), Create(curve), run_time=1.5)
            self.wait(0.4)

        self.wait(2)
