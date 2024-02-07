<h1 align="center">Colorant 🍇</h1>

### About

Colorant is a highly efficient color aimbot designed to rapidly scan for a range of purple color of the valorant enemy player outlines on your screen and precisely aim/shoot at it, without any interference with the game memory or files of Valorant.

Unlike conventional video game cheats that rely on the process memory to function, Colorant adopt a unique approach by avoiding any memory reading altogether. This innovative approach has the potential to remain undetectable by anti-cheat mechanisms that typically attempt to block memory reads. Additionally, sending input to the video game without triggering any flags can be a challenging aspect to consider.

The primary objective of this project is to showcase a proof of concept, demonstrating the potential of Colorant's novel approach to aimbot technology.

---

![image](https://user-images.githubusercontent.com/82477000/225608740-5f690006-9cc8-4d88-8a60-cda89d0f936f.png)

[![Downloads][downloads-shield]][downloads-link]
[![Discord][discord-shield]][discord-link]
[![Language][language-shield]][language-link]
[![License][license-shield]][license-link]

## Getting started

#### You will need the following prerequisites:
- [ARDUINO LEONARDO](https://www.amazon.com/Arduino-org-A000057-Arduino-Leonardo-Headers/dp/B008A36R2Y)
- [USB HOST SHIELD](https://www.amazon.com/Compatible-Arduino-Support-Android-Function/dp/B0B3TH6H6N)
- [Python](https://www.python.org/)

The initial setup can be a bit challenging, as you will need to set up your Arduino and USB host shield. It is important to note that some USB shields may come unsoldered, so you may need to solder both 5V ports and the bottom 3.3V port to ensure that it works correctly. For further clarification, you can refer to [THIS](https://www.youtube.com/watch?v=nBttwvgNOr8) video.

Next, you will need to download and install Python, with [Version 3.8](https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe) being recommended as it was the version used to develop this project. Once Python is installed, you can download Colorant and install the necessary dependencies by using the command `pip install -r the-requirements.txt`.

To utilize the Arduino board as a computer mouse, you can choose from five different sketches that are located within the [ArduinoSketches](https://github.com/hafyzwithawhy/Colorant/tree/main/ArduinoSketches) folder. Connect the Arduino board to your computer and open the Arduino IDE software. Then, select the appropriate board and port, and upload the desired sketch. By following these steps, you can turn your Arduino board into a functional computer mouse, enabling you to control the cursor and perform clicking functions using the board's hardware. I suggest trying out each of the five sketches to determine which one works best for your mouse.

Note that if you selected a sketch other than [1Arduino](https://github.com/hafyzwithawhy/Colorant/tree/main/ArduinoSketches/1Arduino), you may need to configure [move](https://github.com/hafyzwithawhy/Colorant/blob/674355e95507c455ec14c4a6f5c11271d889a71e/mouse.py#L31) and [click](https://github.com/hafyzwithawhy/Colorant/blob/674355e95507c455ec14c4a6f5c11271d889a71e/mouse.py#L36) functions to make it compatible with your Arduino sketch. The Colorant code is currently optimized for the [1Arduino](https://github.com/hafyzwithawhy/Colorant/tree/main/ArduinoSketches/1Arduino) sketch, so adjustments may be necessary for other sketches.

With the prerequisites and dependencies installed, you can now run the `main.py` file, which is the main entry point of the program. You do not need to make any changes to the code, as it is ready to use.

By following these steps, you can enjoy using Colorant to quickly and accurately aim and shoot within your favorite valorant gamemode.

## Configuration
You can customize Colorant to suit your preferences:

- Enemy outlines should be set to PURPLE, as this is how the color aimbot operates.
- The FOV size can be adjusted by editing the value located [Here](https://github.com/hafyzwithawhy/Colorant/blob/836189fb99fa8d6906569103d58a75b4ab98b760/main.py#L8), please note that the existing code is optimized for the use of a 50 FOV, so adjustments to the code may be required to ensure proper functionality for other fov sizes.
- Modify keybinds by changing the virtual-key codes in [This](https://github.com/hafyzwithawhy/Colorant/blob/836189fb99fa8d6906569103d58a75b4ab98b760/colorant.py#L26) function. Refer to [This](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes) link for virtual-key codes.

By making these adjustments, you can fine-tune Colorant to suit your preferences and optimize its performance within the game.
## Support

If you require support or have any questions regarding Colorant, please feel free to join the community Discord:

[![Discord Banner 2][discord-banner]][discord-link]

I would like to express my sincere appreciation and give due credit to the program Firepro, which served as a significant inspiration for the development of my Project Colorant. Furthermore, I would like to clarify that the Arduino sketches incorporated within this project were not coded by me.

## Contributing

Contributions are welcome from the community, and if you have any suggestions or encounter any issues, please do not hesitate to open an [issue](https://github.com/hafyzwithawhy/Colorant/issues) in the repository and provide as much detail as possible. Additionally, if you find this project helpful or interesting, please give it a ⭐.

## Disclaimer

> **Note**
It is important to note that this project is intended for EDUCATIONAL PURPOSES ONLY, and should be used at YOUR OWN RISK.

> **Note**
Although the project is undetectable, this does not mean that it is not bannable. I do not condone any form of hacking, as it can ruin the game experience for both yourself and other players. This project was created solely to demonstrate the possibility of using an Arduino and a simple Python script to "cheat" within a video game.

> **Warning**
It is important to note that while the current implementation may be undetectable, Riot Games could still take action against the current source code itself. To minimize the risk of detection, it is advisable to modify the existing code or create a unique implementation based on the same concept. 

[discord-shield]: https://img.shields.io/discord/1102647720981831750?color=purple&label=Support&logo=discord&logoColor=white&style=for-the-badge
[discord-link]: https://discord.gg/P92kGvubRd
[discord-banner]: https://discordapp.com/api/guilds/1102647720981831750/widget.png?style=banner2

[downloads-shield]: https://img.shields.io/github/downloads/hafyzwithawhy/Colorant/total?color=purple&logo=GitHub&style=for-the-badge
[downloads-link]: https://github.com/hafyzwithawhy/Colorant/releases/latest

[language-shield]: https://img.shields.io/github/languages/top/hafyzwithawhy/Colorant?color=purple&logo=python&logoColor=white&style=for-the-badge
[language-link]: https://www.python.org/

[license-shield]: https://img.shields.io/github/license/hafyzwithawhy/Colorant?color=purple&logo=github&style=for-the-badge
[license-link]: https://github.com/hafyzwithawhy/Colorant/blob/main/LICENSE
