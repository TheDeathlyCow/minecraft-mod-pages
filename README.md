# Minecraft Mod Pages

This repo stores the mod pages for my mods (Frostiful, Scorchful, Thermoo, etc). Each mod is stored in its own folder along with image assets.

## Auto Update Script

The [auto update script](./auto-update.py) will automatically update the descriptions on the Modrinth pages when run. It requires a Modrinth Personal Access Token with at least `write_project` permissions to be stored in the environment variable `MODRINTH_KEY`, which can be done locally by placing a `.env` file in the root of this folder with the following format:

```
MODRINTH_KEY={your access token here}
```

This file will be ignored by Git and not included in any pushed versions of this repo.

## License

This auto update script is released under the MIT license in case anyone out there wants to use any of the code themselves.
