# Stellaris Permanent Autosaves

Ever felt like you wanted to go back in time in Stellaris, but realized you didn't have a save game for then? Stellaris Permanent Autosaves will preserve the game's regularly generated savefiles, allowing you a timeline into your nation's past.

The following installation process _assumes you use Windows_. Additionally, this small project is only tested for Windows.

## Installation

Time to complete: **2 minute**

### Prerequisites:

- Install [Python](https://www.python.org/)
  - You also need `pip`. If you installed Python the "normal" way (via an installer or smth on their website), pip should be auto-installed (test with `pip --version`)

If you install and see no results, restart your terminal.


### Clone this repository:

```bash
git clone https://github.com/natnuo/stellaris-permanent-autosaves.git
```

### Install watchdog:

```bash
pip install watchdog
```

### Locate your relavant savegames folder:

Your saves are stored, by default, at `Documents > Paradox Interactive > Stellaris > save games`. Choose the folder that corresponds to your relavant playthrough.

Copy the full path. This path may appear as illustrated below, though other formats are also possible.

```
C:\Users\myUser\OneDrive\Documents\Paradox Interactive\Stellaris\save games\prikkiimperium_551126668
```

### Start the program:

Execute the `main.py` Python file (double click). When prompted for the save directory to watch, paste the full path obtained above. Now, keep the program open. Every time you want to preserve your autosaves, simply start `main.py`, paste in the relavant path, and enjoy~~
