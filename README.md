# The Most Polish Landscape (App)

This application is part of "The Most Polish Landscape" project, an interactive art installation that creates Polish landscapes in real-time, based on audience interaction. The project uses AI models (SPADE) to generate unique landscape interpretations. 

## Requirements

- Python 3.7 or higher
- SDL2 libraries
  - Linux: `sudo apt install libsdl2-2.0-0`
  - macOS: `brew install sdl2`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/speplinski/tmpl-app.git
cd tmpl-app
```

2. Install the package in development mode:
```bash
pip install -e .
```

## Assets Preparation

Download the required assets (images, overlays, videos):

```bash
chmod +x download_assets.sh
./download_assets.sh
```

## Usage

Run the application with selected monitor:

```bash
# Use main display (usually 0)
tmpl-app --monitor 0

# Use secondary display (usually 1)
tmpl-app --monitor 1
```

## Key Features

- Resolution: 3840x1280
- Smooth transitions between frames and sequences
- Multi-monitor support

## Project Structure

```
tmpl_app/
├── config/     # Configuration and settings
├── core/       # Core SDL2 and rendering functionality
├── players/    # Image sequence and video playback
└── utils/      # Utilities and statistics
```