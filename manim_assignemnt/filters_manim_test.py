from manim import *
import numpy as np

class FilterBasics(Scene):
    def make_wave(self, clean=True):
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[-2, 2, 1],
            x_length=9,
            y_length=3,
            tips=False,
        ).to_edge(DOWN)

        if clean:
            graph = axes.plot(lambda x: np.sin(3*x), color=BLUE)
        else:
            graph = axes.plot(
                lambda x: np.sin(3*x) + 0.4*np.sin(25*x),
                color=RED
            )

        return axes, graph

    def construct(self):
        title = Text("Filter Basics", font_size=44)
        subtitle = Text("Signal → FFT → Filter → Comparison", font_size=28).next_to(title, DOWN)

        self.play(Write(title), Write(subtitle))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(subtitle))

        # Part 1: noisy signal
        question1 = Text("1. What is in the signal?", font_size=34).to_edge(UP)
        axes, noisy = self.make_wave(clean=False)

        self.play(Write(question1))
        self.play(Create(axes), Create(noisy), run_time=3)
        self.wait(5)

        noise_label = Text("Noisy signal = desired signal + high-frequency noise", font_size=25).next_to(axes, UP)
        self.play(Write(noise_label))
        self.wait(6)

        self.play(FadeOut(noise_label), FadeOut(question1))

        # Part 2: FFT idea
        question2 = Text("2. FFT shows the frequencies inside the signal", font_size=30).to_edge(UP)
        bars = VGroup()

        heights = [1.6, 0.5, 1.1, 0.4, 0.8]
        labels = ["5 Hz", "15 Hz", "50 Hz", "80 Hz", "Noise"]

        for i, h in enumerate(heights):
            bar = Rectangle(width=0.45, height=h, fill_opacity=0.8)
            bar.shift(LEFT*3 + RIGHT*i*1.5 + DOWN*0.5)
            label = Text(labels[i], font_size=20).next_to(bar, DOWN)
            bars.add(VGroup(bar, label))

        self.play(Write(question2))
        self.play(LaggedStart(*[GrowFromEdge(b[0], DOWN) for b in bars], lag_ratio=0.25))
        self.play(LaggedStart(*[Write(b[1]) for b in bars], lag_ratio=0.25))
        self.wait(8)

        high_noise = SurroundingRectangle(bars[-1], color=YELLOW)
        note = Text("High frequencies are usually noise", font_size=26).to_edge(DOWN)
        self.play(Create(high_noise), Write(note))
        self.wait(7)

        self.play(FadeOut(question2), FadeOut(bars), FadeOut(high_noise), FadeOut(note), FadeOut(axes), FadeOut(noisy))

        # Part 3: filter
        question3 = Text("3. A low-pass filter keeps low frequencies", font_size=30).to_edge(UP)

        left_box = Rectangle(width=3, height=1.5).shift(LEFT*4)
        filter_box = Rectangle(width=2.5, height=1.5).shift(ORIGIN)
        right_box = Rectangle(width=3, height=1.5).shift(RIGHT*4)

        left_text = Text("Noisy\nSignal", font_size=26).move_to(left_box)
        filter_text = Text("Low-Pass\nFilter", font_size=26).move_to(filter_box)
        right_text = Text("Cleaner\nSignal", font_size=26).move_to(right_box)

        arrow1 = Arrow(left_box.get_right(), filter_box.get_left())
        arrow2 = Arrow(filter_box.get_right(), right_box.get_left())

        self.play(Write(question3))
        self.play(Create(left_box), Write(left_text))
        self.play(Create(arrow1), Create(filter_box), Write(filter_text))
        self.play(Create(arrow2), Create(right_box), Write(right_text))
        self.wait(10)

        self.play(
            FadeOut(left_box), FadeOut(filter_box), FadeOut(right_box),
            FadeOut(left_text), FadeOut(filter_text), FadeOut(right_text),
            FadeOut(arrow1), FadeOut(arrow2), FadeOut(question3)
        )

        # Part 4: before and after
        before_title = Text("Before Filtering", font_size=28).to_edge(UP).shift(LEFT*3)
        after_title = Text("After Filtering", font_size=28).to_edge(UP).shift(RIGHT*3)

        axes1, noisy2 = self.make_wave(clean=False)
        axes2, clean2 = self.make_wave(clean=True)

        axes1.scale(0.65).shift(LEFT*3 + UP*0.5)
        noisy2.scale(0.65).shift(LEFT*3 + UP*0.5)

        axes2.scale(0.65).shift(RIGHT*3 + UP*0.5)
        clean2.scale(0.65).shift(RIGHT*3 + UP*0.5)

        self.play(Write(before_title), Write(after_title))
        self.play(Create(axes1), Create(noisy2))
        self.play(Create(axes2), Create(clean2))
        self.wait(12)

        comparison = Text(
            "The filter removes fast noise and keeps the smoother signal.",
            font_size=28
        ).to_edge(DOWN)

        self.play(Write(comparison))
        self.wait(10)

        self.play(
            FadeOut(before_title), FadeOut(after_title),
            FadeOut(axes1), FadeOut(noisy2),
            FadeOut(axes2), FadeOut(clean2),
            FadeOut(comparison)
        )

        # Conclusion
        end = Text("Final Idea: FFT helps us see noise. Filters help us remove it.", font_size=30)
        self.play(Write(end))
        self.wait(8)
        self.play(FadeOut(end))