# gr-framebuffer-patch
## About

An automatic patcher for Gravity Rush, enabling the game to run at the full 960x544.

---

## Usage
1. Clone the repository (Adjust binaries for Linux, I don't want to.)
2. Install and open [FAGDec](https://github.com/CelesteBlue-dev/PSVita-RE-tools/tree/master/FAGDec) on your PlayStation Vita
3. Select Gravity Rush with the X button, push X again on `DECRYPT ALL(DONE)`, press O to go back to the main menu, select `[START]Decrypt modules in list`, finally select `START DECRYPT(SELF)`
4. Copy `ux0:/FAGDec/app/PCSA00011/eboot.bin` to the root of the repository
5. Run `main.py`
6. Install [rePatch.skprx](https://github.com/dots-tb/rePatch-reDux0/releases/tag/3.0)
7. Copy the patched `eboot.bin` and `self_auth.bin` into `ux0:/rePatch/PCSA00011/`
8. Launch the game.

## Known issues
Minor frame drops in certain locations/scenes
Dialog images are broken.