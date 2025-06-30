from manim import *
import numpy as np

# Vertical video configuration
config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30

class SpiralInwardField(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Title and equation
        title = Text("Spiral Inward Field", color=WHITE, weight=BOLD).scale(1.2).move_to(UP * 3.5)
        self.play(Write(title))

        equation = MathTex(
            r"\vec{F}(x, y) = \left(",
            r"-y - x, \quad x - y",
            r"\right)",
            color=YELLOW
        ).scale(0.8).next_to(title, DOWN, buff=0.4)
        self.play(Write(equation))

        # Spiral vector field definition
        def spiral_field(pos):
            x, y = pos[:2]
            return np.array([-y - x, x - y, 0])

        # Streamlines
        stream_lines = StreamLines(
            spiral_field,
            x_range=[-4, 4, 0.3],
            y_range=[-4, 4, 0.3],
            stroke_width=1.2,
            max_anchors_per_line=50,
            virtual_time=4,
            dt=0.05,
            color=PURPLE,
        ).scale(0.8).move_to(DOWN * 2.0)

        self.play(Create(stream_lines), run_time=2)
        self.wait()

        # Animate flow
        stream_lines.start_animation(
            flow_speed=1.0,
            time_width=1.2,
            line_anim_class=ShowPassingFlashWithThinningStrokeWidth
        )

        self.wait(6)
