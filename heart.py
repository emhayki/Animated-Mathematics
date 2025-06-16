from manim import *
import numpy as np

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30

class HeartCurve(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Heart Curve", color=WHITE, weight=BOLD).scale(1.2)
        title.move_to(UP * 3.5)

        equation = MathTex(
            r"r = 2 - 2\sin(\theta) + \frac{\sin(\theta)\sqrt{|\cos(\theta)|}}{\sin(\theta) + 1.4}",
            color=YELLOW
        ).scale(0.7)
        equation.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Write(equation))

        axes = PolarPlane(
            size=6.2,
            background_line_style={"stroke_color": GRAY, "stroke_opacity": 0.1}
        ).move_to(DOWN * 2.5)
        self.add(axes)

        def heart(theta):
            sin_t = np.sin(theta)
            cos_t = np.cos(theta)
            r = 2 - 2 * sin_t + (sin_t * np.sqrt(abs(cos_t))) / (sin_t + 1.4)
            r *= 1.5
            x = r * np.cos(theta)
            y = r * np.sin(theta) + 2
            return axes.c2p(x, y)

        curve = VMobject(color=RED, stroke_width=4)
        dot = Dot(color=WHITE).scale(0.5)
        theta_tracker = ValueTracker(0)

        def update_curve(mob):
            t = np.linspace(0, theta_tracker.get_value(), 400)
            points = [heart(val) for val in t]
            if len(points) >= 2:
                mob.set_points_as_corners(points)

        def update_dot(mob):
            mob.move_to(heart(theta_tracker.get_value()))

        curve.add_updater(update_curve)
        dot.add_updater(update_dot)

        theta_label = always_redraw(
            lambda: MathTex(
                r"\theta = " + f"{theta_tracker.get_value():.2f}",
                color=WHITE
            ).scale(0.8).next_to(axes, UP, buff=0.5)
        )

        self.add(curve, dot, theta_label)
        self.play(theta_tracker.animate.set_value(2 * PI), run_time=6, rate_func=linear)
        self.wait(2)
