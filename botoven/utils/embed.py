from __future__ import annotations

import random

import embed_templator
import nextcord


class Embed(embed_templator.Embed):

    def setup(self) -> Embed:
        self.color = int('d95e2c', 16)

        return self.set_author(
            name=f"Requested by {self.ctx.author} 🚀",
            icon_url=self.ctx.author.avatar.url
        )

    def update(self) -> Embed:
        lucky: str = (
            "There was 1 / 1 000 000 chance for this message to show 🍀"
        ) * (not random.randint(0, 1_000_000))

        self.set_footer(
            icon_url=self.client.user.avatar.url,
            text=lucky or '   '.join(
                (
                    "⚙ ABC", f"⏳ {self.client.latency}",
                    f"🔑 {self.ctx.prefix}help"
                )
            )
        )

        return self
