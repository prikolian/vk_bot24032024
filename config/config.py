from dataclasses import dataclass

from environs import Env


@dataclass
class VkBot:
    token: str
    id_group: int


@dataclass
class Config_vk:
    vk_bot: VkBot


def load_vk_config(path: str | None = None):
    env = Env()
    env.read_env(path)
    return Config_vk(vk_bot=VkBot(
        token=env('BOT_VK_TOKEN'),
        id_group=int(env('VK_ID_GROUP'))))
