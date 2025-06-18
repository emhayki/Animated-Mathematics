from manim import *
import numpy as np

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30

class SpiralCurve(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Spiral Curve", color=WHITE, weight=BOLD).scale(1.2)
        title.move_to(UP * 3.3)

        equation = MathTex(r"r = 0.1\theta", color=YELLOW).scale(0.9)
        equation.next_to(title, DOWN, buff=0.4)
        self.play(Write(title), Write(equation))

        axes = PolarPlane(
            size=4.5,
            background_line_style={"stroke_color": GRAY, "stroke_opacity": 0.1}
        ).move_to(DOWN * 1.6)
        self.play(Create(axes))

        def spiral(theta):
            r = theta * 0.1
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            return axes.c2p(x, y)

        curve = VMobject(color=BLUE, stroke_width=3)
        dot = Dot(color=WHITE).scale(0.5)
        theta_tracker = ValueTracker(0)

        curve.add_updater(
            lambda m: m.set_points_as_corners(
                [spiral(t) for t in np.linspace(0, theta_tracker.get_value(), 500)]
            )
        )
        dot.add_updater(lambda m: m.move_to(spiral(theta_tracker.get_value())))

        theta_display = always_redraw(
            lambda: MathTex(
                rf"\theta = {theta_tracker.get_value():.2f}",
                color=YELLOW
            ).scale(0.8).next_to(equation, DOWN, buff=0.4)
        )

        self.add(curve, dot, theta_display)
        self.play(theta_tracker.animate.set_value(18 * PI), run_time=8, rate_func=linear)
        self.wait(2)
