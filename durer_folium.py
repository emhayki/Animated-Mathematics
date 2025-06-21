from manim import *
import numpy as np

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30

class DurerFoliumImplicit(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("The Dürer Folium", color=WHITE, weight=BOLD).scale(1.2)
        title.move_to(UP * 3.5)

        formula = MathTex(
            r"a^4 y^2 + 4(x^2 + y^2)^3 - 4a^2(x^2 + y^2)^2 = 0",
            color=YELLOW
        ).scale(0.8).next_to(title, DOWN, buff=0.4)

        self.play(Write(title), Write(formula))

        axes = Axes(
            x_range=[-11, 11],
            y_range=[-11, 11],
            x_length=6,
            y_length=6,
            axis_config={"color": GRAY},
            tips=False
        ).move_to(DOWN * 2.0)
        self.play(Create(axes))

        a_values = [3, 4, 5, 6, 7, 8, 9, 10]
        colors = color_gradient([BLUE, TEAL, GREEN, YELLOW, ORANGE, RED], len(a_values))

        a_label = MathTex("a = 0", color=YELLOW).scale(0.85)
        a_label.next_to(formula, DOWN, buff=0.4)
        self.play(Write(a_label))

        for i, a in enumerate(a_values):
            new_label = MathTex(f"a = {a}", color=YELLOW).scale(0.85)
            new_label.move_to(a_label.get_center())

            def f(x, y):
                r2 = x**2 + y**2
                return (a**4) * y**2 + 4 * r2**3 - 4 * (a**2) * r2**2

            curve = axes.plot_implicit_curve(
                lambda x, y: f(x, y),
                color=colors[i],
                stroke_width=2.5,
                min_depth=0.01
            )

            self.play(Transform(a_label, new_label), Create(curve), run_time=1.2)
            self.add(curve)
            self.wait(0.2)

        self.wait(2)
