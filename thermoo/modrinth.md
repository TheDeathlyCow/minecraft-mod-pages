# Thermoo - Temperature and Environment API

[![](https://media.githubusercontent.com/media/TheDeathlyCow/minecraft-mod-pages/main/frostiful/assets/try_frostiful.svg)](https://modrinth.com/mod/frostiful)

[![](https://media.githubusercontent.com/media/TheDeathlyCow/minecraft-mod-pages/main/scorchful/assets/try_scorchful.svg)](https://modrinth.com/mod/scorchful)

Thermoo is a temperature and environment library mod for Minecraft, targeting the Fabric and Quilt ecosystems. It is meant to help provide compatibility between mods and datapacks that use temperature as a core mechanic, such as Frostiful or Scorchful. Using this mod on its own will have no gameplay or visual effects. It is designed to be used by Mods written in both Java and Kotlin, as well as Datapacks through Commands and other registries.

# Developer Features and Wiki

Thermoo provides a number of useful features for developers of temperature mods and datapacks, including:
* A unified framework for dealing with Temperature and Wetness/Soaking
* Cross-compatibility with other Thermoo mods, without needing to specify direct compatibility patches
* Powerful datapack-based Environment API
* Data-driven temperature effects
* Event-driven configuration of default item attributes
* Robust API for working with unit-agnostic temperature records (like Celsius and Fahrenheit)
* Integration with Seasons mods
* Powerful commands
* Extensive customizability for your own mods
* Can run Server-side only with [Polymer](https://modrinth.com/mod/polymer)

Thermoo has an extensive developer wiki on GitHub, available [here](https://thermoo.thedeathlycow.com/). If you have trouble with something, feel free to ask in my [Discord](https://discord.thedeathlycow.com).

# Configs for Modpack Authors

By itself, Thermoo should have no impact on your game. However, other mods may be installed that rely on features of Thermoo such as temperature effects and freezing. I would also recommend checking out the [API Overview](https://thermoo.thedeathlycow.com/api_overview/) section of the wiki if you want to configure those mods.

# Recommended Mods

Thermoo is the core of my other mods, [Frostiful](https://modrinth.com/mod/frostiful) and [Scorchful](https://modrinth.com/mod/scorchful). If you want to see Thermoo in action, be sure to check it out!

# License and Porting

Thermoo is licensed under LGPLv3. It is a mod developed for the Fabric and Quilt mod loaders on modern versions of Minecraft. Older versions will only be supported according to the [LTS Policy](https://github.com/TheDeathlyCow/thermoo?tab=readme-ov-file#lts-policy). I have no plans to port to other loaders such as NeoForge or Bukkit.

