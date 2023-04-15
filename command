CMD Commands:

For Python 3.9:
python -m pip install kivy[base] kivy_examples
python -m pip install pygame

For Python 3.7 and lower:
python -m pip install --upgrade pip wheel setuptools
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer
python -m pip install kivy.deps.angle
python -m pip install pygame
python -m pip install kivy

For Python 3.8:
pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/
python -m pip install pygame